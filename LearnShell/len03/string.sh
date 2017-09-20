#!/bin/bash

# 字符串运算符

a="abc"
b="efg"

if [ $a = $b ]
then
	echo "a = b"
else
	echo "a != b"
fi

if [ -z $a ]
then
	echo "-z $a: 字符串长度为0"
else
	echo "-z $a: 字符串长度不为0"
fi

if [ $a ]
then
	echo "$a: 字符串为空串"
else
	echo "字符串不为空"
fi
