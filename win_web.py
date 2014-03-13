import gtk,webkit
win=gtk.Window()
web=webkit.WebView()
win.add(web)
web.open('http://google.com/')
win.show_all()
def enter_notify(*a):
    print 'enter'
def leave_notify(*a):
    print 'leave'
    
win.connect("enter_notify_event", enter_notify)
win.connect("leave_notify_event", leave_notify)
gtk.main()
