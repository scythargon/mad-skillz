import gtk,gobject

def dest(*a):
    print '1'
    gobject.timeout_add(500,dest2)

def dest2(*a):
    print 2
    win.add(l)
    win.show_all()

win = gtk.Window()
win.connect("delete_event", dest)
l = gtk.Label('wertety')
win.add(l)
win.show_all()

gtk.main()
