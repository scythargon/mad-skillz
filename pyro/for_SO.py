from daemon import runner
import Pyro4
import sys
import time 

Pyro4.config.HMAC_KEY='topsecret'

class ADaemon():
    def __init__(self,pid_file,handler):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  pid_file
        self.pidfile_timeout = 5
        self.handler=handler
    def run(self):
        print "Ready."
        self.handler()

class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)

greeting_maker=GreetingMaker()
daemon=Pyro4.Daemon()                 # make a Pyro daemon
uri=daemon.register(greeting_maker)   # register the greeting object as a Pyro object

variant=sys.argv[1]  #both|pyro|(start|stop) #daemon

if variant == 'both':
    print 'Pyro & Daemon example'
    print "Pyro is ready. Server uri =", uri      # print the uri so we can use it in the client later
    sys.argv[1]='start'#dont worry about 'zombi' daemons - daemon dont start in this case:( no apocalipsys:(
    runner.DaemonRunner(ADaemon('/tmp/tmp.pid',daemon.requestLoop)).do_action()

elif variant=='pyro':
    print 'Pyro example'
    print "Pyro is ready. Server uri =", uri      # print the uri so we can use it in the client later
    daemon.requestLoop()
elif variant=='start' or variant=='stop':
    print 'Daemon example'
    def testf():
        while True:
            print 'daemon works fine'
            time.sleep(3)
    runner.DaemonRunner(ADaemon('/tmp/tmp.pid',testf)).do_action()
else:
    print 'usage: both|pyro|(start|stop) #daemon'
