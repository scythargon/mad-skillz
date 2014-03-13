import os,time,thread,sys
#import wnck
#time.sleep(0.3)
#wnck.window_get(58720313).activate(999999999999)
#screen = wnck.screen_get_default()
#wnck.window_get(58720313L).activate(9999999999)

time.sleep(1.5)
os.system('xdotool key space')
time.sleep(4)
jump_pause=(1.7,0.4,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27,0.27)
jump_num=0
def jump(*a):
    global jump_num
    while True:
        time.sleep(jump_pause[jump_num])
        print jump_num,': ',jump_pause[jump_num]
        os.system('xdotool key space')
        jump_num+=1
        
def run(*a):
    while True:
        os.system('xdotool key Left')
        time.sleep(0.01)
        os.system('xdotool key Right')
        time.sleep(0.01)

thread.start_new(jump,(0,))
thread.start_new(run,(0,))
time.sleep(6)
print 'good boy!'
sys.exit()
