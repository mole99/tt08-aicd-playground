v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
C {devices/ipin.sym} 290 200 0 0 {name=p1 lab=ui_in[7:0]}
C {devices/opin.sym} 590 260 0 0 {name=p2 lab=uo_out[7:0]}
C {devices/iopin.sym} 590 220 2 1 {name=p3 lab=VGND}
C {devices/iopin.sym} 590 200 2 1 {name=p4 lab=VDPWR}
C {devices/iopin.sym} 230 100 2 0 {name=p5 lab=VAPWR}
C {devices/ipin.sym} 290 220 0 0 {name=p6 lab=uio_in[7:0]}
C {devices/iopin.sym} 1810 540 2 1 {name=p7 lab=ua[7:0]}
C {devices/opin.sym} 590 280 0 0 {name=p8 lab=uio_out[7:0]}
C {devices/opin.sym} 590 300 0 0 {name=p9 lab=uio_oe[7:0]}
C {devices/ipin.sym} 290 240 0 0 {name=p10 lab=ena}
C {devices/ipin.sym} 290 260 0 0 {name=p11 lab=clk}
C {devices/ipin.sym} 290 280 0 0 {name=p12 lab=rst_n}
C {dig_ctrl_top.sym} 440 260 0 0 {name=x1}
C {devices/noconn.sym} 290 300 0 0 {name=l1[7:0]}
C {devices/noconn.sym} 1810 540 0 0 {name=l3}
C {devices/noconn.sym} 230 100 0 1 {name=l12}
C {devices/noconn.sym} 590 320 0 1 {name=l13[7:0]}
C {devices/title.sym} 230 690 0 0 {name=l1 author="Leo Moser"}
C {sky130_leo_ip__levelshifter_up.sym} 1020 220 0 0 {name=x2[7:0]}
C {sky130_leo_ip__levelshifter_down.sym} 1020 420 0 1 {name=x3}
C {sky130_stdcells/buf_16.sym} 1300 330 0 0 {name=x4[7:0] VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hvl__ }
