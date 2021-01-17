#! /bin/sh

./service1/entrypoint.py > service1_output.txt

if [-s service1_output.txt]
then
    echo 'Empty output!'
    exit(-1)
else
    echo 'Smoke test passed!'
fi
