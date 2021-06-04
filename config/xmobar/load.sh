#!/bin/bash
load=$(cut -d ' ' -f1 /proc/loadavg)
echo "CPU: $load"
