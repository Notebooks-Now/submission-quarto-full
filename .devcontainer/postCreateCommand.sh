#!/bin/bash -v

conda init bash
conda env create -f environment.yml
conda activate lapalma-earthquakes