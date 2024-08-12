![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg)

# AICD Playground

A mixed-signal test project for the analog IC design course at Graz University of Technology.

> [!WARNING]  
> 🚧 This repository is WIP. 🚧

This repository is the top-level and integrates a digital 8-bit controller with some analog IPs such as up/down-levelshifters, an R2R-DAC and a comparator. The IPs are connected in a way that a simple SAR-ADC is formed.

The dependencies are hosted in their own repositories and are linked as submodules under `dependencies/`.

## Clone the Repository

Make sure to also clone the submodules:

	git clone https://github.com/mole99/tt08-aicd-playground.git --recurse-submodules

If you forgot to clone with submodules, you can run the following instead:

	git submodule update --init --recursive

## Assemble the Top-Level

The script `merge.py` uses the KLayout Python API to place all IPs inside the template.

## Run Characterization

[CACE](https://github.com/efabless/cace) is used on the top-level and the analog IPs to run DRC and LVS checks. For some IPs simulations are run under different conditions such as corners and temperature.

To run CACE, simply run:

	cace