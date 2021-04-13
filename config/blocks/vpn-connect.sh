#!/bin/bash

status=$(nmcli connection show | grep Lab | awk {'print $4'})
#if [ $status = "eno1" ]; then
#	notify-send -t 3000 "Connected to Lab"
#else
#	notify-send -t 1000 "Connecting..."
#        nmcli connection up Lab &> /dev/null
#	notify-send -t 3000 "Connection established"
#fi

if [ $status = "eno1" ]; then
	echo " VPN"
else
	echo " VPN"
fi

