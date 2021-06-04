#!/bin/bash

status=$(nmcli connection show | grep Lab | awk {'print $4'})
if [ $status = "eno1" ]; then
	echo "Connected"
else
	:
fi
