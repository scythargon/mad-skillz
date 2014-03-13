#!/usr/bin/env python
import gtk

class DynamicLabel(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        self.set_title("Dynamic Label")
        self.set_size_request(1, 1)
        self.set_default_size(300,300) 
        self.set_position(gtk.WIN_POS_CENTER)

        l = gtk.Label("Dynamic Label" * 10)
        l.set_line_wrap(True)
        l.set_size_request(50, 50)
        #l.connect("size-allocate", self.size_request)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(l, False, False, 0)

        self.add(vbox)
        self.connect("destroy", gtk.main_quit)
        self.show_all()

    def size_request(self, l, s ):
        l.set_size_request(50, 50)

DynamicLabel()
gtk.main()
