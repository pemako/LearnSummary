##### 条件判断

- if...else 语句
```shell
if [ 条件 ]
then
	处理
fi

# 注意 在条件和方括号([]) 之间一定要有空格，否则会报语法错误
```

- if...else..fi
```
if [ 条件 ]
then
	处理
else
	处理
fi
```

- if ... elif ... fi 语句可以对多个条件进行判断语法如下
```shell
if [ 条件1 ]
then
	echo 条件1
elif [ 条件2 ]
then
	echo 条件2
elif [ 条件3 ]
then
	echo 条件3
else
	echo 默认
fi
```

- if test
```shell
# if ... else 语句可以写成一行，以命名的方式运行
#if test $[2*3] -eq $[1+5];then echo "两个数字相等";fi;
#if test 相当于 if [ ]
```

- case...esac 和switch ... case 语句类似
```shell
#case 值 in
#模式1)
#	command1
#	command2
#	;;
#模式2)
#	command1
#	command2
#	;;
#*)
#	command1
#	command2
#	;;
#esac

#case 工作方式如上所示。取值后面必须为关键字 in,每一模式必须以右括号结束。取值可以为变量或常数。
#匹配发现取值符合某一模式后,其间所有命令开始执行直至 ;;。;; 与其他语言中的 break 类似,
#意思是跳到整个 ca se 语句的最后。取值将检测匹配的每一个模式。一旦模式匹配,则执行完匹配模式相应
#命令后不再继续其他模式。如果无一匹配 模式,使用星号 * 捕获该值,再执行后面的命令
#!/bin/bash
echo 'Please input 1 to 4'
echo "Your number is :\c"
read number
case $number in
	1)
		echo "You select 1"
		;;
	2)
		echo "You select 2"
		;;
	3)
		echo "You select 3"
		;;
	4)
		echo "You select 4"
		;;
	*)
		echo "You do not select a number between 1 to 4"
		;;
esac
```
<center>[上一节](../len06)　　　　　　　　　　[下一节](../len08)</center>
