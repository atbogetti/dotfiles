#!/bin/bash
winname=$(xdotool getactivewindow getwindowname)
winlen=${#winname}
if [ -z $winname ]; then
    :
elif [ $winlen -gt 40 ]; then
    echo " ${winname:0:40}..."
elif [ $winlen -le 40 ]; then
    echo " $winname"
fi
