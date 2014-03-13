import gtk,webkit
from transparent import Transparent
win=gtk.Window()
win.set_decorated(False)
web=webkit.WebView()
style = 'background: -webkit-linear-gradient(top, bottom, rgba(0,0,0,1), rgba(0,0,0,0));'
style='background: -webkit-linear-gradient(top, bottom, #ccc, #000); '
style="""background: -webkit-linear-gradient(top, rgba(0,0,200,0.5), rgba(0,0,0,0));"""
web.load_html_string('<html style="'+style+'">eqweqweqwe</html>','file:///')
Transparent.makeTransparent(web)
Transparent.makeTransparent(win)
web.set_transparent(True)
win.add(web)
win.show_all()
win.move(700,30)
#win.show()
gtk.main()
