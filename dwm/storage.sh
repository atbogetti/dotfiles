#!/bin/bash

space=$(df -h | grep "sda2" | awk {'print $4'} | tr -dc '0-9')
echo " $space GB"
