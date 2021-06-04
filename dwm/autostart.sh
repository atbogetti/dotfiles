#!/bin/bash

# Autostart programs for qtile
nitrogen --restore &
dunst -config /home/atb43/.config/dunst/dunstrc_qtile &
picom --config /home/atb43/.config/picom/picom.conf &
xset s off -dpms
xsetroot -cursor_name left_ptr &
dropbox start &
