import sys
from time import sleep
for i in range(100):
    sys.stdout.write('%2s%%' % i) 
    sys.stdout.flush()
    sleep(1)
    sys.stdout.write('\b' * 3)