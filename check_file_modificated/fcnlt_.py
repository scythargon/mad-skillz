import time
import fcntl
import os
import signal

FNAME = "./html.html"

def handler(signum, frame):
    print "File %s modified" % (FNAME,)

signal.signal(signal.SIGIO, handler)
fd = os.open(FNAME,  os.O_RDONLY)
fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
fcntl.fcntl(fd, fcntl.F_NOTIFY)

while True:
    time.sleep(10000)
