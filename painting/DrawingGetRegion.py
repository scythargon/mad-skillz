import gtk,math,cairo
from transparent import Transparent

class PaintBoard (gtk.Window,Transparent):
    def __init__(self):
        gtk.Window.__init__(self) 
        Transparent.__init__(self,(0.0,1.0,0.0,0.3))
        self.set_size_request(200,200)
        self.board=DrawingGetRegion(onlyClick=True)
        self.add(self.board)
        self.show_all()

class Handler():
    """Now implement handle(self,region)"""
    def handle(self,region):
        raise NotImplementedError( "Should have implemented 'handle(list)'" )
        
class DrawingGetRegion(gtk.DrawingArea,Transparent):
    """this class is child of gtk.DrawingArea and Transparent
    Implement this_package.Handler.handle(list) to get region parameters"""
    def __init__(self,handler = None,rgba=None,border=None,onlyClick=False):
        gtk.DrawingArea.__init__(self)
        Transparent.__init__(self)
        self.onlyClick=onlyClick
        self.handler = None
        if handler!= None:
            if isinstance(handler,Handler):
                self.handler=handler
            else:
                raise NotImplementedError( "Your handler dont implement mine:p" )
        if rgba!=None:
            self.rgba=rgba
        self.border=border
        self.connect("expose_event", self.expose)
        if not self.onlyClick: 
            self.connect("motion_notify_event", self.motion_notify_event)
            self.connect("button_press_event", self.button_press_event)
        
        self.connect("button_release_event", self.button_release_event)
        
        self.set_events(gtk.gdk.EXPOSURE_MASK
                                 | gtk.gdk.LEAVE_NOTIFY_MASK
                                 | gtk.gdk.BUTTON_PRESS_MASK
                                 | gtk.gdk.BUTTON_RELEASE_MASK
                                 | gtk.gdk.POINTER_MOTION_MASK
                                 | gtk.gdk.POINTER_MOTION_HINT_MASK)
        self.start_x,self.start_y,self.finish_x,self.finish_y=0,0,0,0
        #self.start_x,self.start_y,self.finish_x,self.finish_y=10,10,100,100
    def setOnlyClickMode(self,arg):
        if arg:
            self.finish_x,self.finish_y=0,0
            if self.get_events() & gtk.gdk.BUTTON_RELEASE_MASK:
                print 'removing events!!!'
                #self.hide()
                self.set_events(gtk.gdk.EXPOSURE_MASK
                                 | gtk.gdk.LEAVE_NOTIFY_MASK
                                 | gtk.gdk.BUTTON_PRESS_MASK
                                 | gtk.gdk.BUTTON_RELEASE_MASK
                                 | gtk.gdk.POINTER_MOTION_MASK
                                 | gtk.gdk.POINTER_MOTION_HINT_MASK)
                self.connect("expose_event", self.expose)
                self.connect('expose-event', self.transparent_expose)
                #self.show()
                print "result is: " +str(self.get_events() & gtk.gdk.BUTTON_RELEASE_MASK)
        if not arg:
            if not (self.get_events() & gtk.gdk.BUTTON_RELEASE_MASK):
                self.set_events(gtk.gdk.EXPOSURE_MASK
                                 | gtk.gdk.LEAVE_NOTIFY_MASK
                                 | gtk.gdk.BUTTON_PRESS_MASK
                                 | gtk.gdk.BUTTON_RELEASE_MASK
                                 | gtk.gdk.POINTER_MOTION_MASK
                                 | gtk.gdk.POINTER_MOTION_HINT_MASK)
            
    def button_release_event(self, widget, event):
        self.finish_x,self.finish_y=event.get_coords()
        if not self.onlyClick:
            self.queue_draw()
        if self.handler!=None:
            self.handler.handle((int(self.start_x),
                                int(self.start_y),
                                int(self.finish_x),
                                int(self.finish_y)))
    def button_press_event(self, widget, event):
        self.start_x,self.start_y=event.get_coords()
        self.finish_x,self.finish_y=event.get_coords()
        if not self.onlyClick:
            self.queue_draw()

    def motion_notify_event(self,widget, event):
        if event.is_hint: #existance of POINTER_MOTION_HINT_MASK mask
            #file:///usr/share/gtk-doc/html/pygtk/class-gdkevent.html
            x, y, state = event.window.get_pointer()
        else:
            x = event.x
            y = event.y
            state = event.state
 
        if state & gtk.gdk.BUTTON1_MASK:
            self.finish_x,self.finish_y=x,y
            self.queue_draw()
        return True
   
    def expose(self, widget, event):
        context = widget.window.cairo_create()
        area=(0,0)+widget.window.get_size()
        context.rectangle(area)
        context.clip()
        self.draw(context)
        #print 'expose da'
        return False
    
    def draw(self,context):
        context.set_source_rgba(0, 0, 1,1)
        context.move_to(self.start_x,self.start_y)
        context.line_to(self.start_x,self.finish_y)
        context.line_to(self.finish_x,self.finish_y)
        context.line_to(self.finish_x,self.start_y)
        context.line_to(self.start_x,self.start_y)
        context.stroke()
        #now border
        if self.border!=None:
            context.set_source_rgba(*self.border)
            x,y=self.window.get_size()
            context.move_to(0,0)
            context.line_to(x,0)
            context.line_to(x,y)
            context.line_to(0,y)
            context.line_to(0,0)
            context.stroke()
        

if __name__ == "__main__":
    window = PaintBoard()
    window.show()
    window.connect("destroy", gtk.main_quit)
    gtk.main()
