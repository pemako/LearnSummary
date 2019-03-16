#!/bin/bash

# 拼接字符串
YOU_NAME="pemako"
GREETING="hello, "$YOU_NAME" !"
GREETING_2="hello, ${YOU_NAME} !"

echo $GREETING $GREETING_2

# 获取字符串长度
# ${#变量名}得到字符串长度
string="abcd"
echo ${#string}

# 截取字符串
# ${变量名:起始:长度}得到子字符串
string="domob is a great company"
echo ${string:0:4}

# 字符串删除
# ${变量名#substring正则表达式}从字符串开头开始配备substring,删除匹配上的表达式
# ${变量名%substring正则表达式}从字符串结尾开始配备substring,删除匹配上的表达式
# 注意：${file##*/},${file%/*} 分别是得到文件名，或者目录地址最简单方法
file="/Users/lena/developer/LearnShell/README.md"
echo $file
echo ${file#/} # Users/lena/developer/LearnShell/README.md
echo ${file##*/} # README.md
echo ${file%/*} # /Users/lena/developer/LearnShell

# 字符串替换
# ${变量/查找/替换值} 一个 "/" 便是替换第一个，"//" 便是替换所有，当查找中出现了"/" 需要转义"\/"表示
echo ${file//\//\\} # \Users\lena\developer\LearnShell\README.md
echo ${file/\/Users\//\~} # ~lena/developer/LearnShell/README.md
