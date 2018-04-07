#!/usr/bin/python

import time

start = time.time()
Time1 = time.strftime('%H:%M:%S')
time.sleep(2)
end = time.time()
Time2 = time.strftime('%H:%M:%S')

print('Time1: ', Time1)
print('Time2: ', Time2)

print(str(end-start))
