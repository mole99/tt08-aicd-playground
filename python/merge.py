import klayout.db as db
import os
import subprocess

from sky130_primlib.contact import make_contact

ly = db.Layout()

layer_licon1_drawing = ly.layer(db.LayerInfo(67, 20))

layer_met1_drawing = ly.layer(db.LayerInfo(68, 20))

layer_met3_drawing = ly.layer(db.LayerInfo(70, 20))

layer_met4_drawing = ly.layer(db.LayerInfo(71, 20))
layer_met4_pin     = ly.layer(db.LayerInfo(71, 16))
layer_met4_label   = ly.layer(db.LayerInfo(71, 5))

li1_m1 = 4
m1_m2 = 5
m2_m3 = 6
m3_m4 = 7
m4_m5 = 8

strap_width = 1.6
strap_height = 212.64

def draw_stripe(x, y, label, width=strap_width, height=strap_height):
    box = db.DBox(0.0, 0.0, width, height).moved(x, y)

    top.shapes(layer_met4_drawing).insert(box)
    top.shapes(layer_met4_pin).insert(box)
    text = db.DText(label, db.DTrans(db.DTrans.R0, x+strap_width/2, y+strap_height/2))
    top.shapes(layer_met4_label).insert(text)

# Must start with "tt_um_"
top_module = "tt_um_tt08_aicd_playground"

# Read the template
lmap = ly.read("../template/tt_analog_2x2_3v3.gds")

# Get the top cell and change the name
top = ly.top_cell()
top.name = top_module

# Get the digital top
ly.read("../dependencies/dig_ctrl/gds/dig_ctrl_top.gds")
dig_ctrl_top = ly.cell('dig_ctrl_top')

# Insert the digital top
top.insert(db.DCellInstArray(dig_ctrl_top.cell_index(),
                                  db.DTrans(db.DTrans.R0, db.DPoint(0, 8.76-5))))

# --- Analog IPs ---

def copy_cell_to_layout(target_layout, cell):
    cell_in_target = target_layout.create_cell(cell.name)
    cell_in_target.copy_tree(cell)
    return cell_in_target

# Get the logo
ly_tmp = db.Layout()
ly_tmp.read("../dependencies/sky130_tug_ip__logo/gds/sky130_tug_ip__logo.gds")
logo_top = ly_tmp.cell('sky130_tug_ip__logo')
logo_top = copy_cell_to_layout(ly, logo_top)

# Insert the logo
top.insert(db.DCellInstArray(logo_top.cell_index(),
                                  db.DTrans(db.DTrans.R0, db.DPoint(210, 5))))

# Get the RDAC
ly_tmp = db.Layout()
ly_tmp.read("../dependencies/sky130_leo_ip__rdac_8bit/gds/sky130_leo_ip__rdac_8bit.gds")
rdac_top = ly_tmp.cell('sky130_leo_ip__rdac_8bit')
rdac_top = copy_cell_to_layout(ly, rdac_top)

# Insert the RDAC
top.insert(db.DCellInstArray(rdac_top.cell_index(),
                                  db.DTrans(db.DTrans.M135, db.DPoint(300+13.925, 168+52.895))))

# VGND VIA
for x in [312]:
    for layer in [m1_m2, m2_m3, m3_m4]:
        gen = make_contact(
            via_index=layer, 
            w=strap_width, h=51.41+2
        )
        gen.produce(top, db.DTrans(312 +2/2, 170-0.64 + 51.41/2-2))

# Get levelshifter up 1.8V -> 3.3V
ly_tmp = db.Layout()
ly_tmp.read("../dependencies/sky130_leo_ip__levelshifter/gds/sky130_leo_ip__levelshifter_up.gds")
lvlshifter_up = ly_tmp.cell('sky130_leo_ip__levelshifter_up')
lvlshifter_up.flatten(-1, True) # TODO flatten or else: (hvdifftap.21)
lvlshifter_up = copy_cell_to_layout(ly, lvlshifter_up)

# Insert levelshifter up
for i in range(8):
    top.insert(db.DCellInstArray(lvlshifter_up.cell_index(),
                                      db.DTrans(db.DTrans.R0, db.DPoint(180, 215 - i*(8-1.27)))))

# Power strap
draw_stripe(184-2.8, 6.24, 'VDPWR', height=strap_height+2.745)
draw_stripe(184, 6.24, 'VGND', height=strap_height+2.745)
draw_stripe(190, 6.24, 'VAPWR', height=strap_height+2.745)

# Add power vias
for i in range(8):
    gen = make_contact(
        via_index=m3_m4, 
        w=strap_width, h=1
    )
    gen.produce(top, db.DTrans(182, 216 - 0.025 + 5.15 - i*6.73))
    
    gen = make_contact(
        via_index=m3_m4, 
        w=strap_width, h=1
    )
    gen.produce(top, db.DTrans(182 + 2.8, 216 - 0.025 - i*6.73))
    
    gen = make_contact(
        via_index=m3_m4, 
        w=strap_width, h=1
    )
    gen.produce(top, db.DTrans(182 + 8.8, 216 - 0.025 + 5.15 - i*6.73))

# Add wiring and vias
for i in range(8):
    box = db.DBox(0.0, 0.0, 2.5, 0.3).moved(194.39, 218.135 - i*6.73)
    top.shapes(layer_met3_drawing).insert(box)

    for index in [li1_m1, m1_m2, m2_m3]:
        gen = make_contact(
            via_index=index, 
            w=2, h=0.3
        )
        gen.produce(top, db.DTrans(197, 218.135 + 0.3/2 - i*6.73))
    

# Get levelshifter down 3.3V -> 1.8V
ly_tmp = db.Layout()
ly_tmp.read("../dependencies/sky130_leo_ip__levelshifter/gds/sky130_leo_ip__levelshifter_down.gds")
lvlshifter_down = ly_tmp.cell('sky130_leo_ip__levelshifter_down')
lvlshifter_down = copy_cell_to_layout(ly, lvlshifter_down)

# Insert levelshifter down
top.insert(db.DCellInstArray(lvlshifter_down.cell_index(),
                                  db.DTrans(db.DTrans.R180, db.DPoint(185+24.49-0.7-2.8, 38+20))))

# VGND VIA
gen = make_contact(
    via_index=m3_m4, 
    w=strap_width, h=1
)
gen.produce(top, db.DTrans(200.2 + strap_width/2, 37.0 + 0.5 - 0.035 + 20))

# VDPWR VIA
gen = make_contact(
    via_index=m3_m4, 
    w=strap_width, h=1
)
gen.produce(top, db.DTrans(200.2 + strap_width/2 - 2.8, 37.0 + 0.5 - 0.035 - 6.645 + 20))

# HVL buffers!
pdk_root = os.getenv('PDK_ROOT', '~/.volare')
hvl_path = os.path.join(pdk_root, 'sky130A/libs.ref/sky130_fd_sc_hvl/gds/sky130_fd_sc_hvl.gds')

ly_tmp = db.Layout()
ly_tmp.read(hvl_path)

sky130_fd_sc_hvl__buf_4 = ly_tmp.cell('sky130_fd_sc_hvl__buf_4')
sky130_fd_sc_hvl__buf_4 = copy_cell_to_layout(ly, sky130_fd_sc_hvl__buf_4)

# Insert buf_4
for i in range(8):
    top.insert(db.DCellInstArray(sky130_fd_sc_hvl__buf_4.cell_index(),
                                      db.DTrans(db.DTrans.R180, db.DPoint(200 + 4.8, 218 - 1.665 + 0.25 + 0.9 + 3.17 - i*(8-1.27) - 0.4))))
    
    box = db.DBox(0.0, 0.0, 3, 0.3).moved(194.39 + 3.25, 218.135 - i*6.73)
    top.shapes(layer_met1_drawing).insert(box)
    
    gen = make_contact(
        via_index=li1_m1, 
        w=0.33, h=0.34,
        make_bot=False
    )
    gen.produce(top, db.DTrans(200.75, 218.3 - i*6.73))
    
    gen = make_contact(
        via_index=li1_m1, 
        w=1.2, h=0.34,
        make_bot=False
    )
    gen.produce(top, db.DTrans(204.1, 218.6 - i*6.73))
    
    gen = make_contact(
        via_index=m1_m2, 
        w=1.2, h=0.34
    )
    gen.produce(top, db.DTrans(204.1, 218.6 - i*6.73))
    
    # Connect VPWR with tap
    box = db.DBox(0.0, 0.0, 4.8, 0.74).moved(200, 218 - 1.665 + 0.25 - i*(8-1.27) - 0.115 + 3.56 - 0.4)
    top.shapes(layer_met1_drawing).insert(box)
    
    # Connect VGND with tap
    box = db.DBox(0.0, 0.0, 4.8, 0.74).moved(200, 218 - 1.665 + 0.25 - i*(8-1.27) - 0.115 - 0.4)
    top.shapes(layer_met1_drawing).insert(box)

    # VPWR VIA
    for index in [m1_m2, m2_m3]:
        gen = make_contact(
            via_index=index, 
            w=strap_width, h=0.74
        )
        gen.produce(top, db.DTrans(200 + 1, 218 - 1.665 + 0.25 - i*(8-1.27) - 0.115 + 3.56 + 0.37  - 0.4))

    # VGND VIA
    for index in [m1_m2, m2_m3]:
        gen = make_contact(
            via_index=index, 
            w=strap_width, h=0.74
        )
        gen.produce(top, db.DTrans(200 + 3.8, 218 - 1.665 + 0.25 - i*(8-1.27) - 0.115 + 3.56 + 0.37 - 3.56  - 0.4))

# VGND, VPWR VIAs
for x in [200, 202.8]:
    gen = make_contact(
        via_index=m3_m4, 
        w=strap_width, h=51.41
    )
    gen.produce(top, db.DTrans(x +2/2, 170-0.64 + 51.41/2))

# Power strap
draw_stripe(220-17, 6.24, 'VAPWR')
draw_stripe(220-17-2.8, 6.24, 'VGND')
draw_stripe(220-17-2.8-2.8, 6.24, 'VDPWR')

# Comparator
ly_tmp = db.Layout()
ly_tmp.read("../dependencies/sky130_leo_ip__comparator/gds/sky130_leo_ip__comparator.gds")
comparator = ly_tmp.cell('sky130_leo_ip__comparator')
comparator = copy_cell_to_layout(ly, comparator)

# Insert levelshifter down
top.insert(db.DCellInstArray(comparator.cell_index(),
                                  db.DTrans(db.DTrans.R270, db.DPoint(250, 100))))

# --- Draw Power Stripes ---

# Draw met4 stripes for VDPWR and VGND
# at the exact same position as in the digital macro
draw_stripe(21.04, 6.24, 'VDPWR')
draw_stripe(24.34, 6.24, 'VGND')
draw_stripe(141.04, 6.24, 'VDPWR')
draw_stripe(144.34, 6.24, 'VGND')

# Draw met4 stripe for VAPWR
draw_stripe(315, 6.24, 'VAPWR')
draw_stripe(315-2.8, 6.24, 'VGND')

# Draw metal for analog pins
for i in range(8):
    box = db.DBox(0.0, 0.0, 0.9, 1.0).moved(0.93 + 19.32*i, 0)
    top.shapes(layer_met4_drawing).insert(box)

# --- Manual Routing ---

# Get the manual routing
ly_tmp = db.Layout()
ly_tmp.read("../gds/manual_routing.gds")
manual_routing = ly_tmp.cell('manual_routing')
manual_routing = copy_cell_to_layout(ly, manual_routing)

# Insert the manual routing
top.insert(db.DCellInstArray(manual_routing.cell_index(),
                                  db.DTrans(db.DTrans.R0, db.DPoint(0, 0))))

# Convert PCells to static # TODO necessary?
ctx = db.SaveLayoutOptions()
ctx.write_context_info = False

# Flatten top cell one level
#ly.top_cell().flatten(1, True)

# --- Output ---

# Create directories
if not os.path.exists('../gds/'):
    os.makedirs('../gds/')
if not os.path.exists('../lef/'):
    os.makedirs('../lef/')

# Write the GDS
ly.write(f"../gds/{top_module}.gds", ctx)

# Generate the LEF file using magic

PDK_ROOT = os.getenv('PDK_ROOT', '~/.volare')
PDK = os.getenv('PDK', 'sky130A')

os.environ['PDK_ROOT'] = PDK_ROOT
os.environ['PDK'] = PDK

gds_in = f'../gds/{top_module}.gds'
lef_out = f'../lef/{top_module}.lef'

rcfile = os.path.join(PDK_ROOT, PDK, 'libs.tech', 'magic', f'{PDK}.magicrc')

magic_input = ''
magic_input += f'gds read {gds_in}\n'
magic_input += f'load {top_module}\n'
magic_input += f'select top cell\n'# {top_module}\n'

# Power

for label in ['VGND', 'VDPWR', 'VAPWR']:
    #magic_input += f'port {label} make\n'
    magic_input += f'port {label} class inout\n'
    magic_input += f'port {label} use power\n'

# Analog

for label in [f'ua\\[{i}\\]' for i in range(8)]:
    magic_input += f'port {label} class inout\n'
    magic_input += f'port {label} use signal\n'

# Output

for label in [f'uo_out\\[{i}\\]' for i in range(8)]:
    magic_input += f'port {label} class output\n'
    magic_input += f'port {label} use signal\n'

for label in [f'uio_out\\[{i}\\]' for i in range(8)]:
    magic_input += f'port {label} class output\n'
    magic_input += f'port {label} use signal\n'

for label in [f'uio_oe\\[{i}\\]' for i in range(8)]:
    magic_input += f'port {label} class output\n'
    magic_input += f'port {label} use signal\n'

# Input

for label in ['rst_n', 'ena', 'clk']:
    magic_input += f'port {label} class input\n'
    magic_input += f'port {label} use signal\n'

for label in [f'ui_in\\[{i}\\]' for i in range(8)]:
    magic_input += f'port {label} class input\n'
    magic_input += f'port {label} use signal\n'

for label in [f'uio_in\\[{i}\\]' for i in range(8)]:
    magic_input += f'port {label} class input\n'
    magic_input += f'port {label} use signal\n'

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
