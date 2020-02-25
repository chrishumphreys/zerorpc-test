#!/bin/bash

if [ "$1" == "" ]; then
    echo "Please specify number of clients to run"
    exit 0
fi

number=$1

x=1
while [ $x -le $number ]
do
  python client.py --port=4000 --method=simple
  x=$(( $x + 1 ))
done