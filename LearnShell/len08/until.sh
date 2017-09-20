#!/bin/bash

# 使用until命令输出0-9

a=0
until [ ! $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done
