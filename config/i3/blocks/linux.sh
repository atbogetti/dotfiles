#!/bin/bash

kernel=$(uname -a | grep Linux | awk {'print $3'} | awk 'BEGIN { FS = "-" } ; { print $1 }')
echo " Arch-${kernel}"
