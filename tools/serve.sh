#!/bin/bash

if [ $# -eq 0 ]; then
    echo -e "\nYou need to provide a filename!\n"
    exit 1
fi

# Make sure we clean up after Ctl-C
trap ctrl_c INT
function ctrl_c() {
    rm tmp.ipynb
    rm tmp.slides.html
    exit 1
}

# First make sure the notebook is executed
jupyter nbconvert $1 --to notebook --execute --output tmp.ipynb
# Start Jupyter serve
jupyter nbconvert tmp.ipynb --to slides --post serve

