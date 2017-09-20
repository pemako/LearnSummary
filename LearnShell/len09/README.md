#####  函数

- Shell函数必须先定义后才能使用，格式如下
```shell
# 方式一
function_name(){
	list of commands
	[return value]	
}

# 方式二
function function_name(){
	list of commands
	[return value]
}

# 调用函数只需要给出函数名，不需要加括号
# 函数返回值，可以显示增加return语句；如果不加，会将最后一条命令运行结果作为返回值
# Shell 函数的返回值只能是整数，一般用来表示函数执行成功与否，0表示成，其它值表示失败
# 如果要让函数返回一个字符串，往往会得到错误提示："numberic argument required"
# 如一定要返回字符串，可以先定义一个变量，用来接收函数的计算结果
```

```shell
#!/bin/bash

# 无返回值得函数
Hello(){
	echo "Url: https://github.com/pemako/LearnShell"
}

# 调用
Hello # 输出 Url: https://github.com/pemako/LearnShell

# 有返回值的函数
funcWithReturn(){
	echo "The function is to get the sum of two numbers..."
	echo -n "Input first number:"
	read number
	echo -n "Input another number:"
	read anotheNum
	echo "The two numbers are $number and $anotheNum!"
	return $(($number + $anotheNum))
}

funcWithReturn

ret=$?
echo "The sum of two numbers is $ret!"


# 函数的嵌套
NumberOne(){
	echo "Url: https://github.com/pemako/LearnShell"
	NumberTwo
}

NumberTwo(){
	echo "Url: https://google.com"
}

NumberOne
```

- 函数删除
函数可以像删除变量一样使用 unset命令，不过要加上 .f 选项，格式如下
```shell
unset .f function_name
```

- 函数参数
调用函数的时候可以向其传递参数。在函数体内部，通过$n 的形式来获取参数的值
```shell
#注意,$10 不能获取第十个参数,获取第十个参数需要 ${10}。当 n>=10 时,需要使用 ${n} 来获取参数
funWithParam(){
	echo "The value of the first parameter is $1 !"
	echo "The value of the second parameter is $2 !"
	echo "The value of the tenth parameter is $10 !"
	echo "The value of the tenth parameter is ${10} !"
	echo "The value of the eleventh parameter is ${11} !"
	echo "The amount of the parameters is $# !" # 参数个数
	echo "The string of the parameters is $* !" # 传递给函数的所有参数
}

funWithParam 1 2 3 4 5 6 7 8 9 34 73
```
<center>[上一节](../len08)　　　　　　　　　　[下一节](../len10)</center>
