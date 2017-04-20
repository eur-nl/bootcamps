#!/bin/bash

# Can't do anything without the filename
if [ $# -eq 0 ]; then
    echo -e "\nYou need to provide a filename!\n"
    exit 1
fi

# Make sure we can escape the indefinite loop (?)
trap ctrl_c INT
function ctrl_c() {
    kill -9 $PID
    rm tmp.ipynb
    rm tmp.slides.html
    exit 1
}

# First make sure the notebook is executed
jupyter nbconvert $1 --to notebook --execute --output tmp.ipynb
# Start Jupyter serve, remember PID
jupyter nbconvert tmp.ipynb --to slides --post serve &
PID="$!"
echo "PID = $PID"

# Wait server to actually finish
sleep 3

# Get the IDs with $ xdotool selectwindow
echo "Select the Jupyter Notebook window"
JUPYT_ID=`xdotool selectwindow`
echo "Select the slides window"
SLIDE_ID=`xdotool selectwindow`

while true; do
    # Wait for save, kill process
    inotifywait -e close_write $1
    kill -9 $PID

    # First make sure the notebook is executed
    jupyter nbconvert $1 --to notebook --execute --output tmp.ipynb
    # Restart Jupyter serve, remember PID
    jupyter nbconvert tmp.ipynb --to slides --post serve --ServePostProcessor.open_in_browser=False &
    PID="$!"
    echo "PID = $PID"

    # Wait server to actually finish
    sleep 3
    
    # Refresh window, and back to notebook
    xdotool windowactivate --sync $SLIDE_ID 
    xdotool key  "ctrl+r"
    xdotool windowactivate --sync $JUPYT_ID
done

