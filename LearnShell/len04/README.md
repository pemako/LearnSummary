##### shell 字符串

- 单引号
 - 单引号字符串的限制：单引号里面的字符都会原样输出，单引号字符串中的变量是无效的；单引号中不能出现单引号(对单引号转义也不行)
`str='this is a string'`
- 双引号
 - 双引号中可以有变量，双引号里可以转义字符
```shell
YOU_NAME='pemako'
str="Hello, \"$YOU_NAME\""
```
- 获取字符串长度
```shell
string="pemako"
echo ${#string}
```

- 截取字符串
```shell
string="domob is a great company"
echo ${string:0:4}

- 字符串删除
```shell
file="/Users/lena/developer/LearnShell/README.md"
echo ${file##*/}
echo ${file%/*} # /Users/lena/developer/LearnShell
```
- 字符串替换
echo ${file//\//\\}
echo ${file/\/Users\//\~}

```shell
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
```

<center>[上一节](../len03)　　　　　　　　　　[下一节](../len05)</center>
