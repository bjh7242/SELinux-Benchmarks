#!/bin/bash

if [ ! -p p1 ]; then
	echo "Creating p1 pipe..."
	mkfifo p1
fi

if [ ! -p p2 ]; then
	echo "Creating p2 pipe..."
	mkfifo p2
fi

if [ ! -f 256b ]; then
	echo "Creating 256 byte file (256b)..."
	dd if=/dev/urandom of=256b bs=256 count=1 status=none
fi

if [ ! -f 1k ]; then
	echo "Creating 1k byte file (1k)..."
	dd if=/dev/urandom of=1k bs=1k count=1 status=none
fi

if [ ! -f 4k ]; then
	echo "Creating 4k byte file (4k)..."
	dd if=/dev/urandom of=4k bs=1k count=4 status=none
fi
