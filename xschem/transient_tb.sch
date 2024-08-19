v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
B 2 130 1160 930 1560 {flags=graph
y1=0
y2=1.8
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=-5e-09
x2=9.5e-08
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node="clk
out_p
out_n"
color="4 5 12"
dataset=-1
unitx=1
logx=0
logy=0
rainbow=0}
B 2 750 630 1550 1030 {flags=graph
y1=0
y2=1.8
ypos1=0
ypos2=1.8
divy=5
subdivy=1
unity=1
x1=-5e-09
x2=9.5e-08
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0


dataset=-1
unitx=1
logx=0
logy=0
rainbow=1
digital=1

color="4 5 6"
node="clk
rst_n
uo_out0"}
N 50 150 50 170 {
lab=GND}
N 50 50 50 90 {
lab=vss}
N 130 150 130 170 {
lab=GND}
N 50 170 50 190 {
lab=GND}
N 130 50 130 90 {
lab=avdd}
N 50 170 130 170 {
lab=GND}
N 210 150 210 170 {
lab=GND}
N 130 170 210 170 {
lab=GND}
N 210 50 210 90 {
lab=dvdd}
N 290 150 290 170 {
lab=GND}
N 210 170 290 170 {
lab=GND}
N 290 50 290 90 {
lab=clk}
N 370 150 370 170 {
lab=GND}
N 290 170 370 170 {
lab=GND}
N 370 50 370 90 {
lab=rst_n}
C {tt_um_tt08_aicd_playground.sym} 450 360 0 0 {name=x1}
C {devices/vsource.sym} 50 120 0 0 {name=V0 value=0 savecurrent=false}
C {devices/gnd.sym} 50 190 0 0 {name=l4 lab=GND}
C {devices/vsource.sym} 130 120 0 0 {name=V2 value=3.3 savecurrent=false}
C {devices/lab_wire.sym} 50 50 0 0 {name=p3 sig_type=std_logic lab=vss}
C {devices/lab_wire.sym} 130 50 0 0 {name=p5 sig_type=std_logic lab=avdd}
C {devices/vsource.sym} 210 120 0 0 {name=V1 value=1.8 savecurrent=false}
C {devices/lab_wire.sym} 210 50 0 0 {name=p11 sig_type=std_logic lab=dvdd}
C {sky130_fd_pr/corner.sym} 380 520 0 0 {name=CORNER only_toplevel=false corner=tt}
C {devices/launcher.sym} 360 670 0 0 {name=h5
descr="Load transient data" 
tclcommand="xschem raw_read $netlist_dir/transient_tb.raw tran"
}
C {devices/simulator_commands_shown.sym} 720 70 0 0 {name=COMMANDS
simulator=ngspice
only_toplevel=false 
value="

.temp 27

.control
    * .spiceinit for use with Skywater PDK and ngspice KLU
    set ngbehavior=hsa     ; set compatibility for reading PDK libs
    set skywaterpdk        ; skip some checks for faster lib loading
    set ng_nomodcheck      ; don't check the model parameters
    set num_threads=8      ; CPU processor cores available
    option noinit          ; don't print operating point data
    option klu             ; select KLU as matrix solver
    optran 0 0 0 10p 2n 0  ; don't use dc operating point, but transient op

    *save clk rst_n uo_out0
    save all


    * transient simulation
    options method=gear
    tran 10p 100n

    *save all
    *save clk rst_n uo_out[0]
    write transient_tb.raw
.endc
"}
C {devices/vsource.sym} 290 120 0 0 {name=V3 value="pulse 0 1.8 0 1p 1p 10n 20n" savecurrent=false}
C {devices/lab_wire.sym} 290 50 0 0 {name=p1 sig_type=std_logic lab=clk}
C {devices/lab_wire.sym} 600 300 0 1 {name=p2 sig_type=std_logic lab=avdd}
C {devices/lab_wire.sym} 600 320 0 1 {name=p4 sig_type=std_logic lab=dvdd}
C {devices/lab_wire.sym} 600 340 0 1 {name=p6 sig_type=std_logic lab=vss}
C {devices/lab_wire.sym} 300 360 0 0 {name=p7 sig_type=std_logic lab=clk}
C {devices/lab_wire.sym} 300 340 0 0 {name=p8 sig_type=std_logic lab=dvdd}
C {devices/vsource.sym} 370 120 0 0 {name=V4 value="pwl 0 1.8 40n 1.8 40.1n 0" savecurrent=false}
C {devices/lab_wire.sym} 370 50 0 0 {name=p9 sig_type=std_logic lab=rst_n}
C {devices/lab_wire.sym} 300 300 0 0 {name=p10 sig_type=std_logic lab="8*vss"}
C {devices/lab_wire.sym} 300 320 0 0 {name=p12 sig_type=std_logic lab="8*vss"}
C {devices/lab_wire.sym} 300 380 0 0 {name=p13 sig_type=std_logic lab=rst_n}
C {devices/lab_wire.sym} 600 360 0 1 {name=p14 sig_type=std_logic lab=uo_out[7:0]}
C {devices/lab_wire.sym} 600 380 0 1 {name=p15 sig_type=std_logic lab=uio_out[7:0]}
C {devices/lab_wire.sym} 600 400 0 1 {name=p16 sig_type=std_logic lab=uio_oe[7:0]}
C {devices/lab_wire.sym} 600 420 0 1 {name=p17 sig_type=std_logic lab=ua[7:0]}
C {devices/noconn.sym} 600 360 0 1 {name=l1}
C {devices/noconn.sym} 600 380 0 1 {name=l2}
C {devices/noconn.sym} 600 400 0 1 {name=l3}
C {devices/noconn.sym} 600 420 0 1 {name=l5}
