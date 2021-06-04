#!/bin/bash

scrot /tmp/lock.png
convert -blur 0x4 /tmp/lock.png /tmp/blur.png
rm /tmp/lock.png
i3lock -i /tmp/blur.png -u
