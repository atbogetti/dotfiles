#!/bin/bash

artist=$(playerctl -s metadata artist)
title=$(playerctl -s metadata title)
if [ -z "$artist" ]; then
	:
else 
	printf "   $title - $artist |"
fi
