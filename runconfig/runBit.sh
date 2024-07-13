#!/usr/bin/env bash

./runPython.sh ../src/mazeMain.py -b "$@" | tee test.log
echo compare against golden...
diff golden/test.log test.log
