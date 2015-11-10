#!/usr/bin/env python
# This script measures the number of times two processes can exchange an increasing integer through a pipe
# Adapted from: http://www.roman10.net/named-pipe-in-linux-with-a-python-example/

import os
import time

rPipe = "./p1"	# write pipe
wPipe = "./p2"	# read pipe
value = 0

# create pipe if it doesn't exist
try: 
	os.mkfifo(wPipe)
	os.mkfifo(rPipe)
except OSError:
	pass

# read value from pipe, if null write 1
print "opening wPipe"
w = open(wPipe, 'w')
w.write("1")
w.close()

# enter while loop and wait for input
# start timer, increment value read, write that value back to the pipe
print "creating timeout..."
timeout = time.time() + 10		# timeout ends in 10 seconds
while True:
	# read the new value
	r = open(rPipe, 'r')
	newVal = r.read()
	r.close()
	# if the new value is > the original, set the original to the new one
	if newVal > value:
		value = newVal
		print "New value = " + str(value)
		w = open(wPipe, 'w')
		w.write(value+1)
		w.close()
		# exit the while loop when the timer reaches 10 seconds
		if time.time() > timeout:
			break
		
