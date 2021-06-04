#!/bin/bash

volume=$(pamixer --get-volume)
mute=$(pamixer --get-mute)
if [ $mute = 'true' ]; then
	#echo " 0%"
	echo "mute"
elif [ $mute = 'false' ]; then
	$echo " $volume%"
	echo "VOL: $volume%"
fi
