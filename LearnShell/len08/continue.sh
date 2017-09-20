#!/bin/bash

# continue 命令与 break 命令类似,只有一点差别,它不会跳出所有循环,仅仅跳出当前循环
# 在嵌套循环中continue 命令后根上一个整数，表示跳出第几次循环
for j in 0 5
do
	q=`expr $j % 2`
	if [ $q -eq 0 ]
	then
		echo "number is an even number!"
		continue
	else
		echo "found odd number"
	fi
done
