#!/bin/bash

dropbox=$(top -b -n 1 | grep "dropbox")
slack=$(top -b -n 1 | grep "slack")
zoom=$(top -b -n 1 | grep "zoom")

if [[ -n "$dropbox" ]] && [[ -n $slack ]] && [[ -n $zoom ]]; then
	echo "    "
elif [[ -n "$dropbox" ]] && [[ -n $slack ]] && [[ -z $zoom ]]; then
	echo "  "
elif [[ -z $dropbox ]] && [[ -n $slack ]] && [[ -n $zoom ]]; then
	echo "  "
elif [[ -n $dropbox ]] && [[ -z $slack ]] && [[ -n $zoom ]]; then
	echo "  "
elif [[ -n "$dropbox" ]] && [[ -z $slack ]] && [[ -z $zoom ]]; then
	echo " "
elif [[ -z "$dropbox" ]] && [[ -n $slack ]] && [[ -z $zoom ]]; then
	echo " "
elif [[ -z "$dropbox" ]] && [[ -z $slack ]] && [[ -n $zoom ]]; then
	echo ""
else
	:
fi
