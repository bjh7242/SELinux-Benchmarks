#!/usr/bin/env python
# Measures the number of times a shell script can be executed 8 times concurrently in 1 minute

import os
import time
import sys

counter = 0
timeout = time.time() + 60	# 60 seconds from now
#timeout = time.time() + 5 # 5 seconds from now

while True:
	if time.time() > timeout:
		break
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	os.system("./sed.sh &")
	counter+=1

print "Counter: " + str(counter)
