#!/bin/bash

file="/Users/lena/developer/LearnShell/README.md"

if [ -r $file ]
then
	echo "$file 可读"
else
	echo "$file 不可读"
fi


if [ -s $file ]
then
	echo "$file 不为空"
else
	echo "$file 为空文件"
fi

