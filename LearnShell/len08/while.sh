#!/bin/bash

COUNTER=0
while [ $COUNTER -lt 5 ]
do
	COUNTER=`expr $COUNTER + 1`
	echo $COUNTER
done

echo 'Type <CTRL -D>to terminate'
echo -n 'enter your most liked film:'
while read FILM
do
	echo "Yeah! greate file the $FILM"
done
