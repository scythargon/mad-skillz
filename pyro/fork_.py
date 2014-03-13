#!/usr/bin/env python

"""A basic fork in action"""

import os,sys

sys.argv.insert(1,'qwe')
print sys.argv
exit()
def my_fork():
    child_pid = os.fork()
    if child_pid == 0:
        print "Child Process: PID# %s" % os.getpid()
        si = file('/dev/null', 'r')
        #os.dup2(si.fileno(), sys.stdin.fileno())
        a=raw_input('123')
    else:
        print "Parent Process: PID# %s" % os.getpid()

if __name__ == "__main__":
    my_fork()
