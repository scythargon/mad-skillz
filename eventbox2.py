#!/usr/bin/env python
import gtk
class countdownBox(gtk.EventBox):
    def __init__(self):
        gtk.EventBox.__init__(self)
        self.set_size_request(50,50)
        self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(99999,0,0))
        self.show()

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_size_request(500,500)
e = countdownBox()
#e.show()
hbox = gtk.HBox()
hbox.pack_start(e,False,False)
hbox.show()
hbox.set_size_request(50,50)

vbox = gtk.VBox()
vbox.pack_start(hbox,False,False)
vbox.show()
vbox.set_size_request(50,50)

window.add(vbox)
window.show()
gtk.main()
