#!/bin/bash

# generate 2 random chars, 1 to change and 1 to be the new value
# use sed to modify the original char to the value of the new one
# requires openssl and sed

OLD=`openssl rand -base64 1 | cut -c1`
NEW=`openssl rand -base64 1 | cut -c1`

# if $NEW or $OLD = "/", sed will throw an error
if [ $NEW != "/" ] && [ $OLD != "/" ]
then
	#echo "OLD CHARACTER: $OLD"
	#echo "NEW CHARACTER: $NEW"
	sed -i s/$OLD/$NEW/g text
fi
