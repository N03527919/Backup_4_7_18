#!/usr/bin/python

import random

data = 44
print data

for i in range(1000):
  data = data + round( random.uniform(-0.5,0.5), 2)

print data
