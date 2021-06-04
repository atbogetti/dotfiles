#!/bin/bash
#temp=$(sensors | grep -o -E [+-]?[0-9]*.[0-9]*°C | sed -n '22p' | tr -d '+°C')
temp=$(sensors | grep Package | awk {'print $4'} | tr -d '+°C')
echo " $temp"
