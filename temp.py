#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example layout.py

import pygtk
pygtk.require('2.0')
import gtk
import random,math
 
class EggClockFace(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect("expose_event", self.expose)
        
    def expose(self, widget, event):
        print 'expose'
        self.context = widget.window.cairo_create()
        
        # set a clip region for the expose event
        self.context.rectangle(event.area.x, event.area.y,
                               event.area.width, event.area.height)
        self.context.clip()
        
        self.draw(self.context)
        
        return False
    
    def draw(self, context):
        rect = self.get_allocation()
        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2
        
        radius = min(rect.width / 2, rect.height / 2) - 5
        
        # clock back
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.set_source_rgb(1, 1, 1)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.stroke()
        
        #context.restore()
        
 
class LayoutExample:
    def WindowDestroy(self, widget, *data):
        gtk.main_quit()
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Пример Layout")
        window.set_default_size(300, 300)
        window.connect("destroy", self.WindowDestroy)
        self.layout = gtk.Layout(None, None)
        self.layout.set_size(600, 600)
        
        bark=EggClockFace()
        #self.layout.put(bark, 0, 0)
        #window.add(self.layout)
        window.add(bark)
        window.show_all()

def main():
    # enter the main loop
    gtk.main()
    return 0

if __name__ == "__main__":
    LayoutExample()
    main()
