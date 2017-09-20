##### 循环

- for
```shell
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
```

- while

while 循环用于不断执行一系列命令，也可以从输入文件中读取数据；命令通常为测试条件，其格式如下
```shell
#while command
#do
#	执行条件
#done
#!/bin/bash

COUNTER=0
while [ $COUNTER -lt 5 ]
do
	COUNTER=`expr $COUNTER + 1`
	echo $COUNTER
done

# 读取键盘输入信息，输入信息被设置为变量FILM
echo 'Type <CTRL -D>to terminate'
echo -n 'enter your most liked film:'
while read FILM
do
	echo "Yeah! greate file the $FILM"
done
```

- until
```shell
#until 循环执行一系列命令直到条件为true时停止。until循环与while循环在处理方式上刚好相反。
#until command
#do
#	处理
#done
#command 一般为条件表达式，入股欧返回值为false, 则继续执行循环体内的语句，否则跳出循环
#!/bin/bash
# 使用until命令输出0-9

a=0
until [ ! $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done
```

- break 和 continue
```shell
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
```

```shell
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
```
<center>[上一节](../len07)　　　　　　　　　　[下一节](../len09)</center>
