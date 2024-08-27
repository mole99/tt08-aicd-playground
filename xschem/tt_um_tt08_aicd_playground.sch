v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
T {Digital} 220 30 0 0 0.8 0.8 {}
T {Analog} 810 30 0 0 0.8 0.8 {}
T {Power supply} 130 430 0 0 0.4 0.4 {}
T {Analog pins} 310 430 0 0 0.4 0.4 {}
T {Analog out} 1570 100 0 0 0.4 0.4 {}
T {Analog in} 1440 380 0 0 0.4 0.4 {}
N 980 250 1070 250 {
lab=port_ms_o_ana[7:0]}
N 1150 250 1200 250 {
lab=D[7:0]}
N 1200 90 1200 250 {
lab=D[7:0]}
N 1210 80 1260 80 {
lab=D[0]}
N 1210 100 1260 100 {
lab=D[1]}
N 1210 120 1260 120 {
lab=D[2]}
N 1210 140 1260 140 {
lab=D[3]}
N 1210 160 1260 160 {
lab=D[4]}
N 1210 180 1260 180 {
lab=D[5]}
N 1210 200 1260 200 {
lab=D[6]}
N 1210 220 1260 220 {
lab=D[7]}
N 760 450 780 450 {
lab=port_ms_i}
N 760 250 780 250 {
lab=port_ms_o[7:0]}
N 1440 430 1460 430 {
lab=ua[0]}
N 1560 150 1580 150 {
lab=ua[1]}
N 1580 150 1580 510 {
lab=ua[1]}
N 1440 510 1580 510 {
lab=ua[1]}
N 980 450 1280 450 {
lab=out_p}
N 1580 150 1600 150 {
lab=ua[1]}
N 1340 530 1340 550 {
lab=clk_o}
C {devices/ipin.sym} 130 200 0 0 {name=p1 lab=ui_in[7:0]}
C {devices/opin.sym} 430 260 0 0 {name=p2 lab=uo_out[7:0]}
C {devices/iopin.sym} 210 570 2 0 {name=p3 lab=VGND}
C {devices/iopin.sym} 210 540 2 0 {name=p4 lab=VDPWR}
C {devices/iopin.sym} 210 510 2 0 {name=p5 lab=VAPWR}
C {devices/ipin.sym} 130 220 0 0 {name=p6 lab=uio_in[7:0]}
C {devices/iopin.sym} 390 510 2 0 {name=p7 lab=ua[7:0]}
C {devices/opin.sym} 430 280 0 0 {name=p8 lab=uio_out[7:0]}
C {devices/opin.sym} 430 300 0 0 {name=p9 lab=uio_oe[7:0]}
C {devices/ipin.sym} 130 240 0 0 {name=p10 lab=ena}
C {devices/ipin.sym} 130 260 0 0 {name=p11 lab=clk}
C {devices/ipin.sym} 130 280 0 0 {name=p12 lab=rst_n}
C {dig_ctrl_top.sym} 280 260 0 0 {name=x1}
C {devices/noconn.sym} 380 550 0 1 {name=l3[7:2]}
C {devices/noconn.sym} 1280 490 0 0 {name=l12}
C {devices/title.sym} 380 680 0 0 {name=l1 author="Leo Moser"}
C {sky130_leo_ip__levelshifter_up.sym} 880 250 0 0 {name=x2[7:0]}
C {sky130_leo_ip__levelshifter_down.sym} 880 450 0 1 {name=x3}
C {sky130_leo_ip__rdac_8bit.sym} 1410 150 0 0 {name=x2}
C {sky130_stdcells/buf_4.sym} 1110 250 0 0 {name=x1[7:0] VGND=VGND VNB=VGND VPB=VAPWR VPWR=VAPWR prefix=sky130_fd_sc_hvl__ }
C {sky130_leo_ip__comparator.sym} 1360 470 0 1 {name=x4}
C {bus_connect.sym} 1200 90 0 0 {name=l2 lab=D[0]}
C {bus_connect.sym} 1200 110 0 0 {name=l4 lab=D[1]}
C {bus_connect.sym} 1200 130 0 0 {name=l5 lab=D[2]}
C {bus_connect.sym} 1200 150 0 0 {name=l6 lab=D[3]}
C {bus_connect.sym} 1200 170 0 0 {name=l7 lab=D[4]}
C {bus_connect.sym} 1200 190 0 0 {name=l8 lab=D[5]}
C {bus_connect.sym} 1200 210 0 0 {name=l9 lab=D[6]}
C {bus_connect.sym} 1200 230 0 0 {name=l10 lab=D[7]}
C {devices/lab_wire.sym} 1150 250 0 1 {name=p22 sig_type=std_logic lab=D[7:0]}
C {devices/lab_wire.sym} 210 510 0 1 {name=p23 sig_type=std_logic lab=VAPWR}
C {lab_wire.sym} 1460 430 0 1 {name=p24 sig_type=std_logic lab=ua[0]}
C {lab_wire.sym} 1600 150 0 1 {name=p25 sig_type=std_logic lab=ua[1]}
C {lab_wire.sym} 380 550 0 0 {name=p26 sig_type=std_logic lab=ua[7:2]}
C {lab_wire.sym} 390 510 0 1 {name=p27 sig_type=std_logic lab=ua[7:0]}
C {lab_wire.sym} 760 450 0 0 {name=p28 sig_type=std_logic lab=port_ms_i}
C {lab_wire.sym} 760 250 0 0 {name=p29 sig_type=std_logic lab=port_ms_o[7:0]}
C {lab_wire.sym} 980 250 0 1 {name=p30 sig_type=std_logic lab=port_ms_ana[7:0]}
C {devices/lab_wire.sym} 210 540 0 1 {name=p21 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} 210 570 0 1 {name=p31 sig_type=std_logic lab=VGND}
C {local_vdd.sym} 830 190 0 0 {name=l14 lab=VDPWR}
C {local_vdd.sym} 930 190 0 0 {name=l15 lab=VAPWR}
C {local_gnd.sym} 880 310 0 0 {name=l16 lab=VGND}
C {devices/lab_wire.sym} 430 220 0 1 {name=p13 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} 430 200 0 1 {name=p18 sig_type=std_logic lab=VDPWR}
C {local_gnd.sym} 1410 250 0 0 {name=l17 lab=VGND}
C {local_gnd.sym} 1380 530 0 0 {name=l18 lab=VGND}
C {local_gnd.sym} 880 510 0 0 {name=l19 lab=VGND}
C {local_vdd.sym} 830 390 0 0 {name=l20 lab=VDPWR}
C {local_vdd.sym} 1380 410 0 0 {name=l21 lab=VAPWR}
C {lab_wire.sym} 430 320 2 0 {name=p14 sig_type=std_logic lab=port_ms_o[7:0]}
C {lab_wire.sym} 430 340 2 0 {name=p15 sig_type=std_logic lab=clk_o}
C {lab_wire.sym} 130 300 2 1 {name=p16 sig_type=std_logic lab=port_ms_i}
C {lab_wire.sym} 1340 550 3 0 {name=p17 sig_type=std_logic lab=clk_o}
C {lab_wire.sym} 1120 450 0 1 {name=p19 sig_type=std_logic lab=out_p}
