#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Xlib
import Xlib.display

display = Xlib.display.Display()
root = display.screen().root

windowIDs = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType).value
for windowID in windowIDs:
    window = display.create_resource_object('window', windowID)
    name = window.get_wm_name() # Title
    pid = window.get_full_property(display.intern_atom('_NET_WM_PID'), Xlib.X.AnyPropertyType) # PID
    s = str(pid).split('[')
    if len(s)>1:
        s2=s[1].split('L]')[0]
        print s2
