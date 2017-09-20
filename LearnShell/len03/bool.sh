#!/bin/bash

a=20
b=10

if [ $a -lt 20 -o $b -gt 10 ]
then
	echo "$a<20 or $b>10"
else
	echo "$a >= 20 or $b <= 10"
fi
