#!/usr/bin/env python

import time
import os
import argparse

def copy_file(filename):
	# copy a file 200 times
	for i in range(1,201):
	    #print "Copying file " + str(i)
	    os.system("cp " + filename + " " + filename + "2")
	
def time_copy(filename):
	# Initial time value
	start = time.time()
	
	# copy the file specified on the command line
	copy_file(filename)
	
	# End time value
	done = time.time()
	
	# Calculate the average time difference (over 200 iterations)
	elapsed = (done - start)/200
	return elapsed

def main():
	parser = argparse.ArgumentParser(description='Copies a given file')
	parser.add_argument('-f', dest='filename', help='The input filename', required=True)

	# read arguments (the name of the file to copy)
	args = parser.parse_args()

	# Ensure SELinux is enforcing
	os.system("setenforce 1")

	# Calculate the amount of time it takes to copy a file (selinux enforcing)
	enforcing_time = time_copy(args.filename)
	print "Average time to copy file with SELinux Enforcing: "
	print "    " + str(enforcing_time) + " seconds."

	# Calculate the amount of time it takes to copy a file (selinux permissive)
	os.system("setenforce 0")
	permissive_time = time_copy(args.filename)
	print "Average time to copy file with SELinux Permissive: "
	print "    " + str(permissive_time) + " seconds."

	# Reenable selinux
	os.system("setenforce 1")
	
if __name__ == "__main__":
	main()

