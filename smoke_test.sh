#! /bin/bash

python service1/entrypoint.py > service1_output.txt

VAR=`cat service1_output.txt`

if [ -z "$VAR" ]
then
    echo 'Empty output!'
    exit 1
else
    echo 'Smoke test passed!'
    exit 0
fi
