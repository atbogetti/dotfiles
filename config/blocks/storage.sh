#!/bin/bash

space=$(df -h /home/atb | tail -n 1 | awk {'print $4'})
echo " $space"
