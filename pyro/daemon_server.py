from daemon import runner
import Pyro4
import time
import thread
import os,sys

from daemon import runner

Pyro4.config.HMAC_KEY='lkjhgfdsa'

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

print "Ready. Server uri =", uri      # print the uri so we can use it in the client later
#daemon.requestLoop() 
sys.argv.insert(1,'start')
runner.DaemonRunner(ADaemon('/tmp/a_server.pid',daemon.requestLoop)).do_action()
print 'NS started'
time.sleep(3)
print 'woke up'
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is 12345678.".format(name)

greeting_maker=GreetingMaker()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
print '1'
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(greeting_maker)   # register the greeting object as a Pyro object
print '2'
ns.register("example.greeting", uri)  # register the object with a name in the name server
print '3'

daemon.requestLoop()  

####################3
