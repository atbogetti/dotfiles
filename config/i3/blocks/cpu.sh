#!/bin/bash

cpu=$(mpstat 2 1| grep 'Average' | awk {'print 100 - $12 "%"'})
echo " $cpu"
