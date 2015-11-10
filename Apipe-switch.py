#!/usr/bin/python
import os

# wPipe = write pipe, rPipe = read pipe
wPipe = "./p1"
rPipe = "./p2"
response = ""

# initialize write value with "1"
w = open(wPipe, 'w')
w.write("1")		
w.close()

# enter while loop and wait for value
# while response is not "99999999":
while True:
	r = open(rPipe, 'r')
	response = r.read()
	r.close()
	if int(response) == 99999999:
		print "Response was 99999999"
		break
	w = open(wPipe, 'w')
	newVal = int(response) + 1
	w.write(str(newVal))
	w.close()

print "Done."
