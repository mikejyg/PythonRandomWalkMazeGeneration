#!/usr/bin/env bash

./runPython.sh ../src/mazeMain.py -x 90 -y 48 -r 2 -s maze90x48.txt -f 0,0,89,47 "$@" | tee test90x48.log
echo compare against golden
diff golden/maze90x48.txt maze90x48.txt
diff golden/test90x48.log test90x48.log
