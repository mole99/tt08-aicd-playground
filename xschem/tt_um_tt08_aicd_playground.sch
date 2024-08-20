v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 590 320 800 320 {
lab=port_ms_o[7:0]}
N 800 220 800 320 {
lab=port_ms_o[7:0]}
N 800 220 920 220 {
lab=port_ms_o[7:0]}
N 1580 390 1780 390 {
lab=ua[1]}
N 1740 190 1780 190 {
lab=ua[1]}
N 1780 190 1780 390 {
lab=ua[1]}
N 1180 410 1420 410 {
lab=ua[0]}
N 1120 420 1180 420 {
lab=ua[0]}
N 1180 410 1180 420 {
lab=ua[0]}
N 590 340 720 340 {
lab=#net1}
N 720 340 720 650 {
lab=#net1}
N 720 650 1480 650 {
lab=#net1}
N 1480 490 1480 650 {
lab=#net1}
N 1120 220 1210 220 {
lab=port_ms_o_ana[7:0]}
N 1290 220 1340 220 {
lab=D[7:0]}
N 1340 220 1340 290 {
lab=D[7:0]}
N 1340 290 1380 290 {
lab=D[7:0]}
N 1380 130 1380 290 {
lab=D[7:0]}
N 1390 120 1440 120 {
lab=D[0]}
N 1390 140 1440 140 {
lab=D[1]}
N 1390 160 1440 160 {
lab=D[2]}
N 1390 180 1440 180 {
lab=D[3]}
N 1390 200 1440 200 {
lab=D[4]}
N 1390 220 1440 220 {
lab=D[5]}
N 1390 240 1440 240 {
lab=D[6]}
N 1390 260 1440 260 {
lab=D[7]}
N 260 300 290 300 {
lab=port_ms_i}
N 260 300 260 400 {
lab=port_ms_i}
N 260 420 920 420 {
lab=port_ms_i}
N 260 400 260 420 {
lab=port_ms_i}
C {devices/ipin.sym} 290 200 0 0 {name=p1 lab=ui_in[7:0]}
C {devices/opin.sym} 590 260 0 0 {name=p2 lab=uo_out[7:0]}
C {devices/iopin.sym} 590 220 2 1 {name=p3 lab=VGND}
C {devices/iopin.sym} 590 200 2 1 {name=p4 lab=VDPWR}
C {devices/iopin.sym} 230 100 2 0 {name=p5 lab=VAPWR}
C {devices/ipin.sym} 290 220 0 0 {name=p6 lab=uio_in[7:0]}
C {devices/iopin.sym} 1780 710 2 1 {name=p7 lab=ua[7:0]}
C {devices/opin.sym} 590 280 0 0 {name=p8 lab=uio_out[7:0]}
C {devices/opin.sym} 590 300 0 0 {name=p9 lab=uio_oe[7:0]}
C {devices/ipin.sym} 290 240 0 0 {name=p10 lab=ena}
C {devices/ipin.sym} 290 260 0 0 {name=p11 lab=clk}
C {devices/ipin.sym} 290 280 0 0 {name=p12 lab=rst_n}
C {dig_ctrl_top.sym} 440 260 0 0 {name=x1}
C {devices/noconn.sym} 1790 600 0 1 {name=l3[7:2]}
C {devices/noconn.sym} 1420 450 0 0 {name=l12}
C {devices/title.sym} 230 690 0 0 {name=l1 author="Leo Moser"}
C {sky130_leo_ip__levelshifter_up.sym} 1020 220 0 0 {name=x2[7:0]}
C {sky130_leo_ip__levelshifter_down.sym} 1020 420 0 1 {name=x3}
C {sky130_leo_ip__rdac_8bit.sym} 1590 190 0 0 {name=x2}
C {sky130_stdcells/buf_4.sym} 1250 220 0 0 {name=x1[7:0] VGND=VGND VNB=VGND VPB=VAPWR VPWR=VAPWR prefix=sky130_fd_sc_hvl__ }
C {sky130_leo_ip__comparator.sym} 1500 430 0 1 {name=x4}
C {devices/lab_wire.sym} 1020 280 0 0 {name=p13 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} 1020 480 0 0 {name=p14 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} 1520 490 0 1 {name=p15 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} 1590 290 0 0 {name=p16 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} 970 360 0 0 {name=p17 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} 970 160 0 0 {name=p18 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} 1070 160 0 0 {name=p19 sig_type=std_logic lab=VAPWR}
C {devices/lab_wire.sym} 1520 370 0 1 {name=p20 sig_type=std_logic lab=VAPWR}
C {devices/lab_wire.sym} 1580 470 0 1 {name=p21 sig_type=std_logic lab=VGND}
C {bus_connect.sym} 1380 130 0 0 {name=l2 lab=D[0]}
C {bus_connect.sym} 1380 150 0 0 {name=l4 lab=D[1]}
C {bus_connect.sym} 1380 170 0 0 {name=l5 lab=D[2]}
C {bus_connect.sym} 1380 190 0 0 {name=l6 lab=D[3]}
C {bus_connect.sym} 1380 210 0 0 {name=l7 lab=D[4]}
C {bus_connect.sym} 1380 230 0 0 {name=l8 lab=D[5]}
C {bus_connect.sym} 1380 250 0 0 {name=l9 lab=D[6]}
C {bus_connect.sym} 1380 270 0 0 {name=l10 lab=D[7]}
C {devices/lab_wire.sym} 1290 220 0 1 {name=p22 sig_type=std_logic lab=D[7:0]}
C {devices/lab_wire.sym} 230 100 0 1 {name=p23 sig_type=std_logic lab=VAPWR}
C {lab_wire.sym} 1290 410 0 0 {name=p24 sig_type=std_logic lab=ua[0]}
C {lab_wire.sym} 1780 320 0 0 {name=p25 sig_type=std_logic lab=ua[1]}
C {lab_wire.sym} 1790 600 0 0 {name=p26 sig_type=std_logic lab=ua[7:2]}
C {lab_wire.sym} 1780 710 0 0 {name=p27 sig_type=std_logic lab=ua[7:0]}
C {lab_wire.sym} 510 420 0 0 {name=p28 sig_type=std_logic lab=port_ms_i}
C {lab_wire.sym} 800 220 0 0 {name=p29 sig_type=std_logic lab=port_ms_o[7:0]}
C {lab_wire.sym} 1180 220 0 0 {name=p30 sig_type=std_logic lab=port_ms_o_ana[7:0]}
