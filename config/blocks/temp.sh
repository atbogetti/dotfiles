#!/bin/bash
temp=$(sensors | grep -o -E [+-]?[0-9]*.[0-9]*°C | sed -n '3p' | tr -d '+°C')
echo " $temp"
