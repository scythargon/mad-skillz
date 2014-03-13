#!/usr/bin/env python

"""A basic fork in action"""
import Pyro4
import os,sys,atexit,time,subprocess
from signal import SIGTERM 
#sys.argv.insert(1,'qwe')
#print sys.argv
#exit()
pidfile='/tmp/my_own.pid'
def delpid(self):
    os.remove(self.pidfile)
def stop():
    """
    Stop the daemon
    """
    # Get the pid from the pidfile
    try:
        pf = file(pidfile,'r')
        pid = int(pf.read().strip())
        pf.close()
    except IOError:
        pid = None

    if not pid:
        message = "pidfile %s does not exist. Daemon not running?\n"
        sys.stderr.write(message % pidfile)
        return # not an error in a restart

    # Try killing the daemon process	
    try:
        while 1:
            os.kill(pid, SIGTERM)
            time.sleep(0.1)
    except OSError, err:
        err = str(err)
        if err.find("No such process") > 0:
            if os.path.exists(pidfile):
                os.remove(pidfile)
        else:
            print str(err)
            sys.exit(1)
            
def start():
    try:
        pf = file(pidfile,'r')
        pid = int(pf.read().strip())
        pf.close()
    except IOError:
        pid = None

    if pid:
        message = "pidfile %s already exist. Daemon already running?\n"
        sys.stderr.write(message % pidfile)
        sys.exit(1)
    os.chdir("/") 
    os.setsid() 
    os.umask(0) 
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit from second parent
            sys.exit(0) 
    except OSError, e: 
        sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1) 
    si = file('/dev/null', 'r')
    se = file('/dev/null', 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())		
    os.dup2(se.fileno(), sys.stderr.fileno())

    subprocess.Popen(['python','-m','Pyro4.naming'],env={'PYRO_HMAC_KEY': '123'})
    Pyro4.config.HMAC_KEY='topsecret'
    class GreetingMaker(object):
        def get_fortune(self, name):
            return "Hello, {0}. Here is your fortune message:\n" \
                   "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)

    greeting_maker=GreetingMaker()
    pyro_daemon=Pyro4.Daemon()                 # make a Pyro daemon
    uri=pyro_daemon.register(greeting_maker)   # register the greeting object as a Pyro object
    print "Pyro is ready. Server uri =", uri  
    
    atexit.register(delpid)
    pid = str(os.getpid())
    file(pidfile,'w+').write("%s\n" % pid)

    pyro_daemon.requestLoop()

def my_fork():
    child_pid = os.fork()
    if child_pid == 0:
        print "Child Process: PID# %s" % os.getpid()
        #si = file('/dev/null', 'r')
        #os.dup2(si.fileno(), sys.stdin.fileno())
        #a=raw_input('123')
        if 'start'==sys.argv[1]:
            start()
        elif 'stop'==sys.argv[1]:
            stop()
        else:
            print 'start|stop'
    else:
        print "Parent Process: PID# %s" % os.getpid()
        
if __name__ == "__main__":
    my_fork()
