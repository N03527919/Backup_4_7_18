#!/usr/bin/python

import access

start = "03/23/17"
end = "03/24/17"

output = access.getInfo(start, end)

for index in range(0,len(output)):
  print output[index]
