#!/bin/bash

if [ $desktop = "dwm" ]; then
    echo "yes"
    while true; do
        volume=$(bash ~/.dwm/volume.sh)	    
        updates=$(bash ~/.dwm/update.sh)	    
        temp=$(bash ~/.dwm/temp.sh)	    
        mem=$(bash ~/.dwm/memory.sh)	    
        load=$(bash ~/.dwm/load.sh)	    
        music=$(bash ~/.dwm/music.sh)	    
        space=$(bash ~/.dwm/storage.sh)	    
	xsetroot -name "$music $space | $load | $mem | $temp | $updates | $volume |  $(date +"%a %b %d, %H:%M" ) "
        sleep 1s
    done &
fi

exec $desktop
