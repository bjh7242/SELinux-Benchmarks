#!/usr/bin/python
import os
import time

#communicate with another process through named pipe
#one for receive command, the other for send command
rPipe = "./p1"
wPipe = "./p2"
try:
    os.mkfifo(wPipe)
    os.mkfifo(rPipe)
except OSError:
    pass

r = open(rPipe, 'r')
value = r.read()
r.close()

# create timer and timeout value (10 seconds)
timeout = time.time() + 10
# enter while loop and respond
while True:
	#print "time.time() > timeout ---> " + str(time.time()) + " > " + str(timeout)
	if time.time() > timeout:
		print "Timeout reached"
		w = open(wPipe, 'w')
		w.write("99999999")
		w.close()
		break
		
	w = open(wPipe, 'w')
	newVal = int(value) + 1
	w.write(str(newVal))
	w.close()
	r = open(rPipe, 'r')
	value = r.read()
	#print "Value: " + str(value)
	r.close()
	#time.sleep(1)

print "Final response: " + str(value)
