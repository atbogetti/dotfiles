#!/bin/bash

volume=$(awk -F"[][]" '/Left:/ { print $2 }' <(amixer sget Master))
mute=$(awk -F"[][]" '/Left:/ { print $4 }' <(amixer sget Master))
if [ $mute = 'off' ]; then
	echo "  0%"
elif [ $mute = 'on' ]; then
	echo " $volume"
fi
