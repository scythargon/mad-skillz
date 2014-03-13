#!/usr/bin/python
import gtk, sys, cairo

def hello(a,b):
	print("hello")
win = gtk.Window()
win.set_size_request(100, 100)

l = gtk.Label("I want events.")
e = gtk.EventBox()
e.add(l)
e.add_events(gtk.gdk.BUTTON_PRESS_MASK)
e.connect("button_press_event", hello)
win.add(e)
l.show()
e.show()
win.show()
gtk.main()
