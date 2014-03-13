#! /usr/bin/env python
# -*- coding: utf-8 -*-
import gtk,os,thread
from Xlib import X, display
import Xlib

def getWin(pid_):
    display_ = display.Display()
    root = display_.screen().root
    windowIDs = root.get_full_property(display_.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType).value
    s2=0
    s=0
    #print len(windowIDs)
    for windowID in windowIDs:
        window = display_.create_resource_object('window', windowID)
        name = window.get_wm_name() # Title
        pid = window.get_full_property(display_.intern_atom('_NET_WM_PID'), X.AnyPropertyType) # PID
        s = str(pid).split('[')
       # print pid
        if len(s)>1:
            s2=s[1].split('L]')[0]
            #print s2
            if int(s2)==pid_:
                print "getWin(pid) ok"
                return window
pid=0
class Window:
    def __init__(self, display_, msg):
        global pid
        pid = os.getpid()
        print 'im is',pid
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.display = display.Display()
        self.window.show()
        self.label = gtk.Label('blablabla')
        self.label.show()
        #self.window.add(self.label)
        
        btn = gtk.Button('Click')
        btn.show()
        btn.connect('clicked',self.btn_clicked)
        self.window.add(btn)
        
        try:
            thread.start_new_thread( self.loop, ())
        except:
            print "Error: unable to start thread"

        gtk.main()
        #print "NOOOOO"
        """
        self.display = display_
        self.msg = msg
        self.screen = self.display.screen()
        self.window = self.screen.root.create_window(
            10, 10, 100, 100, 1,
            self.screen.root_depth,
            background_pixel=self.screen.white_pixel,
            event_mask=X.ExposureMask | X.KeyPressMask | X.EnterWindowMask,
            )
        self.gc = self.window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            )
 
        self.window.map()
        """
    def btn_clicked(self,*asd):
        win = getWin(pid)
        #print type(win)
        win.change_attributes(event_mask = X.KeyPressMask | X.EnterWindowMask)
        #print type(self.window)
        print "mask applied"
        
        
    def loop(self):
        
        print 'loop init'
        while True:
            print 'loop'
            e = self.display.next_event()
 
            if e.type == X.Expose:
                self.window.fill_rectangle(self.gc, 20, 20, 10, 10)
                self.window.draw_text(self.gc, 10, 50, self.msg)
            elif e.type == X.KeyPress:
                #raise SystemExit
                print  'hello'
            elif e.type == X.EnterNotify:
                print '.'
            else :
                print '_'
        print 'loop end'
 
 
if __name__ == "__main__":
    Window(display.Display(), "Hello, World!")
