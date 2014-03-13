#!/usr/bin/env python
import cairo
class Transparent:
    def __init__(self,rgba=(.0,.0,.0,.0)):
        Transparent.makeTransparent(self)
        self.rgba=rgba
    @staticmethod
    def transparent_expose (widget, event):
        #print widget
        if 'gtk.Layout' in str(type(widget)):
            cr=widget.bin_window.cairo_create()
        else:
            cr = widget.window.cairo_create()
        cr = widget.window.cairo_create()
        cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.rectangle(event.area)
        cr.fill()
        cr.set_operator(cairo.OPERATOR_OVER)
        cr.set_source_rgba(*widget.rgba)
        cr.rectangle(event.area)
        cr.fill()  
    @staticmethod
    def makeTransparent(thing,rgba=(.0,.0,.0,.0)): 
        thing.rgba=rgba
        thing.transparent_expose=Transparent.transparent_expose
        thing.set_app_paintable(True)
        screen = thing.get_screen()
        rgba = screen.get_rgba_colormap()
        thing.set_colormap(rgba)
        thing.connect('expose-event', thing.transparent_expose)
