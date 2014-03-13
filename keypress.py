#!/usr/bin/python
import pyatspi, time
time.sleep(0.1)
reg = pyatspi.Registry.generateKeyboardEvent
reg(24, None, pyatspi.KEY_PRESSRELEASE) #q
