#!/bin/bash

# break 命令允许跳出所有循环（终止执行后面的所有循环）
# 在嵌套循环中break 命令后根上一个整数，表示跳出第几次循环
while :
do
	echo -n "input a number between 1 to 5:"
	read number
	case $number in 
		1|2|3|4|5)
			echo "You number is $number"
			;;
		*)
			echo "You do not select a number between 1 to 5, game is over!"
			break
			;;
	esac
done

# 如果 i=2 并且j=0 跳出循环
for i in 1 2 3
do
	for j in 0 5
	do
		if [ $i -eq 2 -a $j -eq 0 ]
		then
			break 2
		else
			echo "$i $j"	
		fi
	done
done
