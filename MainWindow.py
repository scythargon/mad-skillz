#!/usr/bin/env python
import gtk,gobject
from transparent import Transparent
from math import ceil
from StandartKeySet import StandartKeySet
class MainWindow(gtk.Window,Transparent):
    def __init__(self):
        gtk.Window.__init__(self)
        Transparent.__init__(self)
        """self.settings = settings_
        self.alpha = self.getProperty(alpha)
        self.bgImage = self.getProperty(bgImage)
        self.bgColor = self.getProperty(bgColor)"""
        #self.window.add(button('key'))
    def hideAndThenShow(self,caller,*time):
        self.hide()
        if len(time)>0:
            time=time[0]
        else:
            time=1000
        gobject.timeout_add(time,self.showAndRetFalse)
    def showAndRetFalse(self):
        self.show()
        return False
    def setupWindow(self):
        
        # Makes the window paintable, so we can draw directly on it
        # This sets the windows colormap, so it supports transparency.
        # This will only work if the wm support alpha channel
        screen = self.get_screen()
        proc=1
        self.set_size_request(int(ceil(screen.get_width()*proc)), int(ceil(screen.get_height()*proc)))
#        if (proc==1):
        self.set_decorated(False)
        self.fullscreen()
        self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
       # win.size_allocate(gtk.gdk.Rectangle(100,100,100,100))
        self.set_accept_focus(False)
        rgba = screen.get_rgba_colormap()
        self.set_colormap(rgba)
        self.size = self.get_size()
        self.rgba = (0.0,1.0,0.0,0.3)
        #self.connect('expose-event', self.expose)
        self.activeKeySet = StandartKeySet(self.get_size(),self)
        self.add(self.activeKeySet)
