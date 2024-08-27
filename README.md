![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/cace/badge.svg)

# AICD Playground

A mixed-signal test project for the analog IC design course at Graz University of Technology.

This repository is the top-level and integrates a digital 8-bit controller with several analog IPs such as up/down-levelshifters, an R2R-DAC and a comparator. The IPs are connected in a way that a simple SAR-ADC is formed.

- [Documentation](docs/tt_um_tt08_aicd_playground.md)
- [Characterization](docs/tt_um_tt08_aicd_playground_layout.md)

The dependencies are hosted in their own repositories and are linked as submodules under `dependencies/`.

- [dig_ctrl](https://github.com/mole99/dig_ctrl) - An 8-bit digital controller
- [sky130_leo_ip__comparator](https://github.com/mole99/sky130_leo_ip__comparator/) - A simple clocked comparator for 3.3V
- [sky130_leo_ip__levelshifter](https://github.com/mole99/sky130_leo_ip__levelshifter) - Simple up-/down-levelshifter for 1.8V/3.3V
- [sky130_leo_ip__rdac_8bit](https://github.com/mole99/sky130_leo_ip__rdac_8bit) - A simple 8-bit R2R-DAC
- [sky130_tug_ip__logo](https://github.com/mole99/sky130_tug_ip__logo) - Logo for TU Graz

## Clone the Repository

Make sure to also clone the submodules:

	git clone https://github.com/mole99/tt08-aicd-playground.git --recurse-submodules

If you forgot to clone with submodules, you can run the following instead:

	git submodule update --init --recursive

## Assemble the Top-Level

The script `merge.py` under `python/` uses the KLayout Python API to place all IPs inside the template. Magic is used to write the LEF file. Most of the wiring is done using this script, but still some parts are manually routed.

## Run Characterization

[CACE](https://github.com/efabless/cace) is used on the top-level and the analog IPs to run DRC and LVS checks. For some IPs simulations are run under different conditions such as corners and temperature.

To run CACE, simply run:

	cace

## License

Copyright 2024 Leo Moser

Licensed under the Apache License, Version 2.0.