#!/bin/bash

#available=$(cat /proc/meminfo | grep "Available" | awk {'print $2'})
#total=$(cat /proc/meminfo | grep "MemTotal" | awk {'print $2'})
#used=$(python -c "print( (1-($available/$total))*100 )")
#rounded=$(echo ${used} | awk '{print int($1+0.5)}')
used=$(free -m | grep Mem | awk {'print $3'})
shared=$(free -m | grep Mem | awk {'print $5'})
mem=$(($used+$shared))
echo "  ${mem} MB"
