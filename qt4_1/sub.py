print "blyat;"
from blessings import Terminal
import gtk,webkit,gobject,sys,os,time,signal,logging

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

t = Terminal()

web=webkit.WebView()
win=gtk.Window()
logging.debug('fuck you Im alive!')
index = 0
finished = False
def finished_cb(web_view,sig,res):
	global finished
	global index
	index += 1
	print index,': ',
	status = web_view.get_property("load-status").value_name
	print t.green_bold+status+t.normal,
	uri = res.get_property("uri")
	print sig,t.bold_blue,uri,t.normal
	if "FINISH" in status and not finished:
		print 'finish'
		finished = True
		gobject.timeout_add(500,drawWindow)
		print 'timeout'
		return 
		web_view.execute_script("$('.aj').eq(1).click()")

	if finished and "pkey" in uri:
		print 'move'
		web_view.execute_script("$('#phone').css('position','fixed')")
		web_view.execute_script("$('#phone').css('left','0px')")
		web_view.execute_script("$('#phone').css('top','0px')")
		drawWindow()


sig = "document-load-finished"
sig = "notify::load-status"
sig2= "resource-load-finished"
#web.connect(sig, finished_cb)
web.connect(sig2, finished_cb)
url = 'http://google.com/'
url = 'http://wool/simple.html'
#url = 'http://www.avito.ru/items/moskva_telefony_acer_liquid_e_ferrari_ferrari_special_edition_91382564'
web.open(url)

win.add(web)

def drawWindow(*a):
    width, height = win.get_size()
    pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, width, height)

    screenshot = pixbuf.get_from_drawable(win.window, win.get_colormap(), 
                                          0, 0, 0, 0, width, height)

    screenshot.save('screenshot.png', 'png')
    print 'screenshot saved'
    gtk.main_quit()
print 'win.show'
win.show_all()
gtk.main()