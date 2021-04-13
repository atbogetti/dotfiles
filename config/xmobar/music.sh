#!/bin/bash

artist=$(playerctl metadata artist)
title=$(playerctl metadata title)
if [ -z $artist ]; then
	echo "No Music"
else 
	echo " $title - $artist"
fi
