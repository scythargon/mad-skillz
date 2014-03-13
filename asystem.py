#!/usr/bin/env python
import gtk,os
def throwKeyPress(key):
    os.system("xdotool key "+key)
