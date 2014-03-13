from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import gobject
import sys
import time

QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))
import sys
import codecs

reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

qtapp = QApplication(sys.argv)


def js(com):
	return browser.webpage.mainFrame().evaluateJavaScript(QString(com))
def check():
	i=0
	stop = 5
	while ((not js("$('#phone').html()").toString().startsWith(QString('<img src="/items'))) and i<stop):
		print i,': ',js("$('#phone').html()").toString()
		time.sleep(0.5)
		i+=1
	print js("$('#phone').html()").toString()
def request_finished():
	print 'loaded'
	js("$('.aj').eq(1).click()")
	#print 'first',js("$('#phone').html()").toString()
	#QTimer().singleShot(0, lambda: check())
	#time.sleep(1)#
	#print 'second',js("$('#phone').html()").toString()
class Browser(QObject):
	def __init__(self):
		self.webpage = QWebPage()
		self.widget = QWebView()
		self.widget.setPage(self.webpage)
		self.connect(self.webpage, SIGNAL("loadFinished(bool)"), lambda: request_finished() )
browser = Browser()
url = 'http://www.avito.ru/items/moskva_telefony_acer_liquid_e_ferrari_ferrari_special_edition_91382564'
browser.webpage.mainFrame().load(QUrl(url))
#browser.resize(320, 240)  
#browser.setWindowTitle("Hello, World!")  
browser.widget.show()
#QCoreApplication.processEvents()
sys.exit(qtapp.exec_())