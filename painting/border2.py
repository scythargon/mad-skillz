import gtk,math,cairo
from transparent import Transparent

class PaintBoard (gtk.Window,Transparent):
    def __init__(self):
        gtk.Window.__init__(self) 
        Transparent.__init__(self,(0.0,1.0,0.0,0.3))
        self.set_size_request(200,200)
        self.board=Board()
        self.add(self.board)
        self.show_all()

class Board(gtk.DrawingArea,Transparent):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        Transparent.__init__(self)
        #self.connect("expose_event", self.expose)
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
        self.start_x,self.start_y,self.finish_x,self.finish_y=10,10,100,100
    def button_release_event(self, widget, event):
        self.finish_x,self.finish_y=event.get_coords()
    def button_press_event(self, widget, event):
        self.start_x,self.start_y=event.get_coords()

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
            self.draw_rectangle()
        return True
   
    def expose(self, widget, event):
        #print "clock"+str(widget)
        self.context = widget.window.cairo_create()
        
        # set a clip region for the expose event
        #self.area=event.area
        self.area=(0,0)+widget.window.get_size()
        self.context.rectangle(self.area)
        self.context.clip()
        
        self.draw(self.context)
        
        return False
    def draw_rectangle(self):
        context=self.window.cairo_create()
        context.set_operator(cairo.OPERATOR_CLEAR)
        context.rectangle((0,0)+self.window.get_size())
        context.fill()        
        context.stroke()        
        context.set_operator(cairo.OPERATOR_OVER)

        context.set_source_rgba(0,0,1,1)
        context.move_to(self.start_x,self.start_y)
        context.line_to(self.start_x,self.finish_y)
        context.line_to(self.finish_x,self.finish_y)
        context.line_to(self.finish_x,self.start_y)
        context.line_to(self.start_x,self.start_y)
        context.stroke()
        self.queue_draw()

        
    def draw(self, *context):
        print 'draw, len=',len(context)
        if len(context)==0:
            #context.restore()
            self.queue_draw()

        else:
            context=context[0]
            context.set_source_rgba(0, 0, 0,0.5)
            context.set_source_rgba(0,0,1,1)
            
            context.move_to(self.start_x,self.start_y)
            context.line_to(self.start_x,self.finish_y)
            context.line_to(self.finish_x,self.finish_y)
            context.line_to(self.finish_x,self.start_y)
            context.line_to(self.start_x,self.start_y)
            context.stroke()

if __name__ == "__main__":
    window = PaintBoard()
    window.show()
    window.connect("destroy", gtk.main_quit)
    gtk.main()
