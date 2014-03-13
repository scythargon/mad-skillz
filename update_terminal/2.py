import sys
import time

f='-\\|/'

for i in range(10):
    sys.stdout.write("\r{0}".format(f[i%4]))
    sys.stdout.flush()
    time.sleep(0.5)
