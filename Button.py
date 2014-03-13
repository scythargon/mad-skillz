#!/usr/bin/env python
import gtk
from transparent import Transparent
import asystem
class button(gtk.EventBox,Transparent):
    STATE_FREE = 'state free'
    STATE_PRESSED = 'state pressed'
    STATE_HOLD = 'state hold'
    def __init__(self,keySet_,key_,is_modificator_ = False):
        gtk.EventBox.__init__(self) 
        Transparent.__init__(self)   
        self.keySet = keySet_
        self.key = key_
        self.freeColor = (0.0, 0.0, 0.5, 0.2)#gtk.gdk.Color('#0ff')
        self.pressedColor = (0.5, 0.0, 0.5, 0.5)#gtk.gdk.Color('#0f0')
        self.holdColor = (0.5, 0.5, 0.0, 0.5)#gtk.gdk.Color('#ff0')
        self.keyState = button.STATE_FREE
        #self.set_size_request(size_,size_)
        #self.modify_bg(gtk.STATE_NORMAL, self.get_colormap().alloc_color("red"))
        self.is_modificator = is_modificator_
        self.label = gtk.Label(self.key)
        self.label.show()
        self.add(self.label)
        self.show()
        #self.set_visible_window(False)
        self.changeBGforState()
        self.connect("button_press_event", self.handleKeyPress)
        self.connect("button_release_event", self.handleKeyRelease)
        
        #self.size = (size_,size_)
        #self.rgba = (0.0,0.0,0.0,1.0)
        
        #self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(self.rgba[0],self.rgba[1],self.rgba[2]))
        return
    def changeBGforState(self):
        if self.keyState == button.STATE_FREE:
            self.rgba = self.freeColor
        elif self.keyState == button.STATE_HOLD:
            self.rgba = self.holdColor
        else : 
            self.rgba = self.pressedColor
        self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(self.rgba[0],self.rgba[1],self.rgba[2]))
    debug = False
    def handleKeyPress(self,window,event):
        just_release=False
        if event.type == gtk.gdk.BUTTON_PRESS:
            if button.debug:
                print 'press'
            if(self.keyState == button.STATE_HOLD):
                self.keySet.holdKeys.remove(self.key)
            else:
                self.emitKeyPress()
            self.keyState = button.STATE_PRESSED
        elif event.type == gtk.gdk._2BUTTON_PRESS:
            self.keyState = button.STATE_HOLD
            self.keySet.holdKeys.append(self.key)
            if button.debug:
                print '2click'
        self.changeBGforState()
        
    def handleKeyRelease(self,window,event):
        if (self.keyState != button.STATE_HOLD):
            self.keyState = button.STATE_FREE
            if button.debug:
                print 'release'
        self.changeBGforState()
    
    def emitKeyPress(self):
        combo =''
        for hold in self.keySet.holdKeys:
            combo += (hold+'+')
        combo+=self.key
        #print combo
        asystem.throwKeyPress(combo)
        
