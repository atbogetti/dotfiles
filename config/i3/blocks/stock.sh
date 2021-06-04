#!/bin/bash
price=$(curl -s https://www.marketwatch.com/investing/stock/gme | grep '<meta name="price" content="' |cut -d'"' -f4)
#echo " $price"
echo "GME $price"
