#!/usr/bin/env python
import gtk


class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        eb = gtk.EventBox()
        #just comment the next str and callback will work
        self.add(eb)
        b=gtk.Button('asd')
        b.show()
        eb.add(b)
        eb.show()
        self.connect('expose-event', self.expose)
        self.show()
    def expose (self,widget, event):
        cr = widget.window.cairo_create()
        print 'expose'
MainWindow()
gtk.main()
        
