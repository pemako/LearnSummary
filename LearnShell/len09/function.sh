#!/bin/bash

Hello(){
	echo "Url: https://github.com/pemako/LearnShell"
}

funcWithReturn(){
	echo "The function is to get the sum of two numbers..."
	echo -n "Input first number:"
	read number
	echo -n "Input another number:"
	read anotheNum
	echo "The two numbers are $number and $anotheNum!"
	return $(($number + $anotheNum))
}

#funcWithReturn

#ret=$?
#echo "The sum of two numbers is $ret!"

NumberOne(){
	echo "Url: https://github.com/pemako/LearnShell"
	NumberTwo
}

NumberTwo(){
	echo "Url: https://google.com"
}

#unset .f NumberTwo
#NumberOne

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


