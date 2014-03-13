from daemon import Daemon
import Pyro4
import sys
import time 

Pyro4.config.HMAC_KEY='topsecret'

class ADaemon(Daemon):
    def post_init(self,handler):
        self.handler=handler
    def run(self):
        print "Ready."
        self.handler()


class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)

greeting_maker=GreetingMaker()
pyro_daemon=Pyro4.Daemon()                 # make a Pyro daemon
uri=pyro_daemon.register(greeting_maker)   # register the greeting object as a Pyro object

variant=sys.argv[1]  #both|pyro|(start|stop) #daemon

if variant == 'both':
    print 'Pyro & Daemon example'
    print "Pyro is ready. Server uri =", uri      # print the uri so we can use it in the client later
    sys.argv[1]='start'#dont worry about 'zombi' daemons - daemon dont start in this case:( no apocalipsys:(
    #runner.DaemonRunner(ADaemon('/tmp/tmp.pid',pyro_daemon.requestLoop)).do_action()
    daemon = ADaemon('/tmp/daemon-example.pid',stdout='')
    daemon.post_init(pyro_daemon.requestLoop)
    if 'start' == sys.argv[2]:
        daemon.start()
    elif 'stop' == sys.argv[2]:
        daemon.stop()
    elif 'restart' == sys.argv[2]:
        daemon.restart()

elif variant=='pyro':
    print 'Pyro example'
    print "Pyro is ready. Server uri =", uri      # print the uri so we can use it in the client later
    pyro_daemon.requestLoop()
elif variant=='start' or variant=='stop':
    print 'Daemon example'
    def testf():
        while True:
            print 'daemon works fine'
            time.sleep(3)
    #runner.DaemonRunner(ADaemon('/tmp/tmp.pid',testf)).do_action()
    daemon = ADaemon('/tmp/daemon-example.pid',stdout='')
    daemon.post_init(testf)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

else:
    print 'usage: both|pyro|(start|stop) #daemon'
