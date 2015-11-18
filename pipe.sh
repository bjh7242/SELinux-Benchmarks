#!/bin/bash
# this script measures how long it takes to push 512 bytes through a pipe
# pv must be installed

# The average data rate to make a 51MB file will be displayed
dd if=/dev/urandom bs=512 count=100000 status=none | pv -a | dd of=file status=none

