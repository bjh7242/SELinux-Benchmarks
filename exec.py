#!/usr/bin/env python
# Measures the number of execl calls and averages it out per second over 5 seconds

import os
import time
import sys

counter = 0
timeout = time.time() + 5

while True:
	if time.time() > timeout:
		break
	newpid = os.fork()
	# if the newpid is 0, the process is a child
	if newpid==0:
		# exec echo 0 and pipe it to /dev/null, then exit
		os.system('exec /bin/echo 0 > /dev/null')
		sys.exit()
	# else, increment the execl counter
	else:
		counter+=1

print "Counter: " + str(counter)
