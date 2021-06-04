#!/bin/bash

cap=$(cat /sys/class/power_supply/BAT0/capacity)
echo " $cap%"
