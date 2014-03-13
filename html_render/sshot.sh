#!/bin/sh
echo "Enter id of the window:"
#read window
#window_id=`xwininfo -name $window | awk '{print $4}' | grep -i 0x`
read window_id
import -window $window_id terminal.jpg
import -window 0x1800004 0x1800004.png
#xwinfo
