#!/bin/bash

for i in `seq -w 00 23`
do 
	echo `expr $i + 100`
done

#for 循环格式如下
#for 变量 in 列表(十一组数字，字符串等)组成的序列每个值通过空格分隔
#do
#	command1
#	command2
#done

# 遍历指定目录下的文件
for i in `ls $HOME/developer/LearnShell`
do
	if [ -f $i ]
	then
		echo $i 是文件
	elif [ -d $i ]
	then
		echo $i 是目录
	else
		echo 未知类型
	fi
done
