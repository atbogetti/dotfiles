#!/bin/bash

bright=$(light -G)
round=$( printf "%.0f" $bright )

echo " $round%"
