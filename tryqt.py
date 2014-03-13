from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import sys
qtapp = QApplication(sys.argv)
browser = QWebPage()
url = 'http://www.avito.ru/items/moskva_telefony_acer_liquid_e_ferrari_ferrari_special_edition_91382564'
browser.mainFrame().load(QUrl(url))
browser.show()
#QCoreApplication.processEvents()
sys.exit(application.exec_())