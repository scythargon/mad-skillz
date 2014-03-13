#!/usr/bin/python 
# -*- coding: utf-8 -*-
import gtk
class MainWin:

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(1)
        self.window.show()
        self.label = gtk.Label('blablabla')
        self.label.show()
        self.window.add(self.label)
        self.window.connect("frame-event", self.blabla)
    def blabla(self):
        print "blabla"    
    def main(self):
        gtk.main()

MainWin().main()
