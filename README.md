# SELinux-Benchmarks
Scripts to test SELinux benchmarks discussed here: https://www.usenix.org/legacy/event/usenix01/freenix01/full_papers/loscocco/loscocco_html/node15.html

To initialize the environment with the required test files, run 
```
./initialize.sh
```
To clean up the unneeded files after the test, run
```
./cleanup.sh
```

## File copy test 
This test determines the amount of time it takes to copy a specified file.
```
python filecopy.py -f 'filename'
```
where filename is '256b', '1k', or '4k' for the respective specified filesizes

## Pipe Test
This test determines the average rate of data pushed through a pipe.
```
./pipe.py
```

## Pipe Switch Test
This test determines how fast an integer can be passed between two scripts while being incremented at each end and written out to a pipe for the other script to read in and write out to a second pipe.
```
python Apipe-switch.py
```
In a second terminal window, run
``` 
python Bpipe-switch.py
```
The Bpipe-switch.py script will run for ten seconds and then send a message to Apipe-switch.py to terminate when the counter runs out. Bpipe-switch.py will then print the value of the incremented integer. 

## Process Creation Test
This test determines how fast a script can fork itself and then exit immediately. It will output the number of times the script forks. It runs for ten seconds and then terminates, printing the number of times it forked before exiting.
``` 
python fork.py
```

## Execl Test
This test counts the number of times the exec call can be made in a five second time span.
```
python exec.py
```

## Shell Script Test
This test executes the sed.sh script which will choose 2 random characters, one to be replaced, and the value to replace it with. It will use sed to replace the first character with the second one in the file 'text.' It will run this script eight times concurrently for 60 seconds.
```
python shell-script.py
```
