#!/usr/bin/env python
# Measures the number of newly forked processes over 10 seconds

import os
import time
import sys

counter = 0
timeout = time.time() + 10

while True:
	if time.time() > timeout:
		break
	newpid = os.fork()
	# if the newpid is 0, the process is a child
	if newpid==0:
		sys.exit()
	# else, increment the execl counter
	else:
		counter+=1

print "Counter: " + str(counter)
