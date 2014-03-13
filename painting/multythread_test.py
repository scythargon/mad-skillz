import thread,time

def print_time(name,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (name, time.ctime(time.time()))
        
thread.start_new_thread( print_time, ('thread-1',2))
thread.start_new_thread( print_time, ('thread-2',4))

a=5
while 1: 
    s=raw_input('s=')
    a+=int(s)
    print a
