import gtk,cairo,gobject
win=gtk.Window()
def deferr(win):
    size=win.window.get_size()
    cr = win.window.cairo_create()
    cr.set_operator(cairo.OPERATOR_CLEAR)
    cr.rectangle((0,0)+size)
    cr.fill()
    cr.set_operator(cairo.OPERATOR_OVER)
    cr.set_source_rgba(0.0,0.0,1,1)
    cr.rectangle(size[0]*0.817,size[1]*0.15,10,10)
    cr.fill()  
    #win.queue_draw()
    print 'ready'
win.set_size_request(300,300)
win.resize(300,300)
win.move(650,30)
win.set_app_paintable(True)
screen = win.get_screen()
rgba = screen.get_rgba_colormap()
win.set_colormap(rgba)
win.show()
gobject.timeout_add(1000,deferr,win)
gtk.main()
