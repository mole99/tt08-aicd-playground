import klayout.db as db
import os
import subprocess

# Must start with "tt_um_"
top_module = "tt_um_tt08_aicd_playground"

ly = db.Layout()

# Read the template
lmap = ly.read("template/tt_analog_2x2_3v3.gds")

# Get the top cell and change the name
top = ly.top_cell()
top.name = top_module

# Get the digital top
ly.read("dependencies/dig_ctrl/gds/dig_ctrl_top.gds")
dig_ctrl_top = ly.cell('dig_ctrl_top')

# Remove met5 layers from the digital cell
"""layer_met5_drawing = ly.layer(db.LayerInfo(72, 20))
layer_met5_pin     = ly.layer(db.LayerInfo(72, 16))
layer_met5_label   = ly.layer(db.LayerInfo(72, 5))
layer_via4_drawing = ly.layer(db.LayerInfo(71, 44))

dig_ctrl_top.clear(layer_met5_drawing)
dig_ctrl_top.clear(layer_met5_pin)
dig_ctrl_top.clear(layer_met5_label)
dig_ctrl_top.clear(layer_via4_drawing)"""

# Remove met3.pin
"""layer_met3_pin     = ly.layer(db.LayerInfo(70, 16))
dig_ctrl_top.clear(layer_met3_pin)"""

# Insert the digital top
top.insert(db.DCellInstArray(dig_ctrl_top.cell_index(),
                                  db.DTrans(db.DTrans.R0, db.DPoint(0, 8.76-5))))

# --- Analog IPs ---

def copy_cell_to_layout(target_layout, cell):
    cell_in_target = target_layout.create_cell(cell.name)
    cell_in_target.copy_tree(cell)
    return cell_in_target

# Get the RDAC
ly_tmp = db.Layout()
ly_tmp.read("dependencies/sky130_leo_ip__rdac_8bit/gds/sky130_leo_ip__rdac_8bit.gds")
rdac_top = ly_tmp.cell('sky130_leo_ip__rdac_8bit')
rdac_top = copy_cell_to_layout(ly, rdac_top)

# Insert the RDAC
top.insert(db.DCellInstArray(rdac_top.cell_index(),
                                  db.DTrans(db.DTrans.R90, db.DPoint(300, 168))))

# Get levelshifter up 1.8V -> 3.3V
ly_tmp = db.Layout()
ly_tmp.read("dependencies/sky130_leo_ip__levelshifter/gds/sky130_leo_ip__levelshifter_up.gds")
lvlshifter_up = ly_tmp.cell('sky130_leo_ip__levelshifter_up')
lvlshifter_up = copy_cell_to_layout(ly, lvlshifter_up)

# Insert levelshifter up
for i in range(8):
    top.insert(db.DCellInstArray(lvlshifter_up.cell_index(),
                                      db.DTrans(db.DTrans.R0, db.DPoint(180, 215 - i*(8-1.27)))))

# Get levelshifter down 3.3V -> 1.8V
ly_tmp = db.Layout()
ly_tmp.read("dependencies/sky130_leo_ip__levelshifter/gds/sky130_leo_ip__levelshifter_down.gds")
lvlshifter_down = ly_tmp.cell('sky130_leo_ip__levelshifter_down')
lvlshifter_down = copy_cell_to_layout(ly, lvlshifter_down)

# Insert levelshifter down
top.insert(db.DCellInstArray(lvlshifter_down.cell_index(),
                                  db.DTrans(db.DTrans.R180, db.DPoint(185, 38))))

# HVL buffers!
pdk_root = os.getenv('PDK_ROOT', '~/.volare')
hvl_path = os.path.join(pdk_root, 'sky130A/libs.ref/sky130_fd_sc_hvl/gds/sky130_fd_sc_hvl.gds')

ly_tmp = db.Layout()
ly_tmp.read(hvl_path)

sky130_fd_sc_hvl__buf_4 = ly_tmp.cell('sky130_fd_sc_hvl__buf_4')
sky130_fd_sc_hvl__buf_4 = copy_cell_to_layout(ly, sky130_fd_sc_hvl__buf_4)

# Insert buf_16
for i in range(8):
    top.insert(db.DCellInstArray(sky130_fd_sc_hvl__buf_4.cell_index(),
                                      db.DTrans(db.DTrans.R0, db.DPoint(200, 218 - 1.665 + 0.25 - i*(8-1.27)))))

# Comparator
ly_tmp = db.Layout()
ly_tmp.read("dependencies/sky130_leo_ip__comparator/gds/sky130_leo_ip__comparator.gds")
comparator = ly_tmp.cell('sky130_leo_ip__comparator')
comparator = copy_cell_to_layout(ly, comparator)

# Insert levelshifter down
top.insert(db.DCellInstArray(comparator.cell_index(),
                                  db.DTrans(db.DTrans.R270, db.DPoint(220, 100))))

# --- Draw Power Stripes ---

def draw_stripe(x, y, label):
    width = 1.6
    height = 212.64

    layer_met4_drawing = ly.layer(db.LayerInfo(71, 20))
    layer_met4_pin     = ly.layer(db.LayerInfo(71, 16))
    layer_met4_label   = ly.layer(db.LayerInfo(71, 5))
    
    box = db.DBox(0.0, 0.0, width, height).moved(x, y)

    top.shapes(layer_met4_drawing).insert(box)
    top.shapes(layer_met4_pin).insert(box)
    text = db.DText(label, db.DTrans(db.DTrans.R0, x+width/2, y+height/2))
    top.shapes(layer_met4_label).insert(text)

# Draw met4 stripes for VDPWR and VGND
# at the exact same position as in the digital macro
draw_stripe(21.04, 6.24, 'VDPWR')
draw_stripe(24.34, 6.24, 'VGND')

# Draw met4 stripe for VAPWR
draw_stripe(315, 6.24, 'VAPWR')

# Draw metal for analog pins
for i in range(8):
    box = db.DBox(0.0, 0.0, 0.9, 1.0).moved(0.93 + 19.32*i, 0)
    layer_met4_drawing = ly.layer(db.LayerInfo(71, 20))
    top.shapes(layer_met4_drawing).insert(box)

# Convert PCells to static # TODO
ctx = db.SaveLayoutOptions()
ctx.write_context_info = False

# Flatten top cell one level
#ly.top_cell().flatten(1, True)

# Create directories
if not os.path.exists('gds/'):
    os.makedirs('gds/')
if not os.path.exists('lef/'):
    os.makedirs('lef/')

ly.write(f"gds/{top_module}.gds", ctx)


# Generate the LEF file using magic

PDK_ROOT = os.getenv('PDK_ROOT', '~/.volare')
PDK = os.getenv('PDK', 'sky130A')

os.environ['PDK_ROOT'] = PDK_ROOT
os.environ['PDK'] = PDK

gds_in = f'gds/{top_module}.gds'
lef_out = f'lef/{top_module}.lef'

rcfile = os.path.join(PDK_ROOT, PDK, 'libs.tech', 'magic', f'{PDK}.magicrc')

magic_input = ''
magic_input += f'gds read {gds_in}\n'
magic_input += f'load {top_module}\n'
magic_input += f'property FIXED_BBOX "0 0 {319240//5} {225760//5}"\n'
magic_input += f'lef write {lef_out} -hide -pinonly\n'

with subprocess.Popen(
    ['magic'] + ['-dnull', '-noconsole', '-rcfile', rcfile],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True,
) as process:

    stdout, stderr = process.communicate(magic_input)
    returncode = process.returncode

    if returncode != 0:
        print(f'Subprocess exited with error code {returncode}')

    print(stdout)
    print(stderr)
