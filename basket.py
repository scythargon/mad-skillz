import os,time
waitT=1.5
betweenT=0.23
t1=0.22
t2=0.45
t3=0.65
t4=0.84
sleep=0.8
time.sleep(waitT)
os.system('xdotool key space')
time.sleep(betweenT)
for i in range(5):
    os.system('xdotool keydown space')
    time.sleep(t1)
    os.system('xdotool keyup space')
    time.sleep(sleep)
    print 1
time.sleep(betweenT)
for i in range(4):
    os.system('xdotool keydown space')
    time.sleep(t2)
    os.system('xdotool keyup space')
    time.sleep(sleep)
    print 2
time.sleep(betweenT)
for i in range(4):
    os.system('xdotool keydown space')
    time.sleep(t3)
    os.system('xdotool keyup space')
    time.sleep(sleep)
    print 3
time.sleep(betweenT)
for i in range(4):
    os.system('xdotool keydown space')
    time.sleep(t4)
    os.system('xdotool keyup space')
    time.sleep(sleep)
    print 2
