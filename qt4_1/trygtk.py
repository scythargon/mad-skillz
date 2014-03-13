import gtk,webkit,gobject,sys,os,time,subprocess

silence_xvfb=True
display='1'
screen='0'
xvfb_timeout=3
'''
use silence_xvfb=False to show frame-buffer errors (debugging)
the display and screen arguments are arbitrary really - but this is the
  X display and screen id's that will be used for the frame buffer.
'''
pidfile = '/tmp/.X%s-lock' % display
redirect = '> /dev/null 2>&1'
if not silence_xvfb:
	redirect = ''
cmd = ' '.join(['Xvfb', ':'+display, '-screen', screen, '1600x1200x24', redirect])
os.system(cmd+' &')

start = time.time()
while(True):
	diff = time.time() - start
	if(diff > xvfb_timeout):
		raise SystemError("Timed-Out waiting for Xvfb to start - {0} sec".format(xvfb_timeout))
	if(os.path.isfile(pidfile)):
		break
	else:
		time.sleep(0.05)

os.putenv('DISPLAY', ':%s' % display)
#subprocess.Popen("python ../webview_daemon/sub_test.py",shell=True,stdout=subprocess.PIPE)
child = subprocess.Popen("python sub.py",shell=True,stdout=subprocess.PIPE)
s=' ' 
while s: 
    s=child.stdout.readline() 
    print s.rstrip()
print 'PARENT again'
