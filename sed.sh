#!/bin/bash

# generate 2 random chars, 1 to change and 1 to be the new value
# use sed to modify the original char to the value of the new one

OLD=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-1};echo;`
NEW=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-1};echo;`

echo "OLD LETTER: $OLD"
echo "NEW LETTER: $NEW"

sed -i s/$OLD/$NEW/g text
