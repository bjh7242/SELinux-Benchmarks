#!/usr/bin/env python
# This script measures the number of times two processes can exchange an increasing integer through a pipe
# Adapted from: http://www.roman10.net/named-pipe-in-linux-with-a-python-example/

import os
import time

rPipe = "./p1"	# read pipe
wPipe = "./p2"	# write pipe
value = 0

# create pipe if it doesn't exist
try: 
	os.mkfifo(wPipe)
	os.mkfifo(rPipe)
except OSError:
	print "OSError... continuing."
	pass

# read value from pipe, if null write 1
#print "opening rPipe"
#r = open(rPipe, 'r')
#rVal = r.read()
#print "rVal = " + str(rVal)
#r.close()


#if rVal is None:
#	print "rVal is null... writing 1"
#	print "opening wPipe"
#	w = open(wPipe, 'w')
#	w.write("1")
#	w.close()

# enter while loop and wait for input
# start timer, increment value read, write that value back to the pipe
#print "value = " + str(value) + " and rVal = " + str(rVal)
print "creating timeout..."
timeout = time.time() + 10		# timeout ends in 10 seconds
while True:
	# read the new value
	r = open(rPipe, 'r')
	rVal = r.read()
	r.close()
	if time.time() > timeout:
		w = open(wPipe, 'w')
		print "Ending timer..."
		w.write("9999999999")
		w.close()
		break
	# if the new value is > the original, set the original to the new one
	if rVal > value:
		value = rVal
		#print "New value = " + str(value)
		w = open(wPipe, 'w')
		newVal = int(value)+1
		print "New value ====== " + str(newVal)
		w.write(str(newVal))
		w.close()
		# exit the while loop when the timer reaches 10 seconds
		
print "Done."
