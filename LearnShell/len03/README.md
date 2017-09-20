#### Shell 替换运算符 及注释

##### Shell 替换

- 命令替换

 - 命令替换是指shell可以先执行命令，将输出结果暂时保存，在适当的地方输出
 - 语法：command 注意是反引号
```shell
#!/bin/bash

# 获取当前的时间并保存到DATE变量中
DATE=`date "+%Y%m%d %H:%M:%S"`
echo $DATE

# 获取当前有多少用户在登陆
USERS=`who | wc -l`
echo $USERS
```

- 变量替换
 - 变量替换可以根据变量的状态（是否为空，是否定义等）来改变它的值
 - 变量替换形式

变量|	说明
------|---------
${var}	|变量本来的值
${var:-word}|	如果变量var为空或者已被删除(unset),那么返回world，但不改变var的值。类似于缺省值 
${var:=word}|	如果变量var为空或者已被删除(unset),那么返回world,并将var的值设置为word
${var:+word}|	如果变量var被定义，那么返回word，但不改变var的值
${var:?message}|	如果变量var为空或已被删除(unset),那么将消息message送到标准错误输出，可以监测变量var 是否可以被正常赋值。若此替换出现在she'll脚本中，脚本将停止运行

```shell
#!/bin/bash

# 如果变量 var 为空或已被删除(unset),那么返回 word,但不改变 var 的值
echo ${var:-"variable is not set"}
echo "1 - value of var is ${var}"

# 如果变量 var 为空或已被删除(unset),那么返回 word,并将 var 的值设置为 word。
echo ${var:="variable is not set"}
echo "2 - value of var is ${var}"

unset var
# 如果变量 var 被定义,那么返回 word,但不改变 var 的值。
echo ${var:+"this is default value"}
echo "3 - value of var is ${var}"

var="Prefix"
echo ${var:+"This is default value"}
echo "4 - value of var is $var"

```

##### 运算符

- 算术运算符

运算符|	说明|	举例
------|-----|------
+	  | 加法|	`expr $a + $b` 结果为 30。
-	  | 减法|	`expr $a - $b` 结果为 10。
*	  |	乘法|	`expr $a \* $b` 结果为  200。
/	  |	除法|	`expr $b / $a` 结果为 2。
%	  |	取余|	`expr $b % $a` 结果为 0。
=	  |	赋值|	a=$b 将把变量 b 的值赋给 a。
==	  |	相等 用于比较两个数字，相同则返回 true。|	[ $a == $b ] 返回 false。
!=	  |	不相等	用于比较两个数字，不相同则返回 true |	[ $a != $b ] 返回 true。

* 乘号(*)前边必须加反斜杠()才能实现乘法运算
* 条件表达式要放在方括号之间,并且要有空格,例如 [$a==$b] 是错误的,必须写成 [ $a == $b ]

```shell
#!/bin/bash

# 算术运算符
a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

# 注意 * 乘号需要转移
val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ] 
then
	echo "a is equal to b"
fi

if [ $a != $b ] 
then
	echo "a is not equal to b"
fi

```

- 关系运算符 关系运算符只支持数字，不支持字符串，除非字符串的值是数字
	
运算符|	说明|	举例
------|-----|------
-eq	| 检测两个数是否相等，相等返回true|		[ $a -eq $b ] // true
-ne | 检测连个数是否相等，不相等返回true|		[ $a -ne $b ] //true
-gt | 检测左边的数是否大于右边，如果是返回true|	[ $a -gt $b ]
-lt | 检测左边的数是否小于右边，如果是返回true|	[ $a -lt $b ]
-ge | 检测左边的数是否大于等于右边，如果是返回true|	[ $a -ge $b ]
-le |检测左边的数是否小于等于右边，如果是返回true|	[ $a -le $b ]
```shell
#!/bin/bash

# 关系运算符只支持数字，不支持字符串，除非字符的值是数字
a=10
b=20

if [ $a -eq $b ]
then
	echo "$a -eq $b : a is equal to b" 
else
	echo "$a -eq $b: a is not equal to b"
fi

if [ $a -ne $b ] 
then
	echo "$a -ne $b: a is not equal to b"
else
	echo "$a -ne $b : a is equal to b"
fi

if [ $a -gt $b ]
then
	echo "$a -gt $b: a is greater than b"
else
	echo "$a -gt $b: a is not greater than b"
fi

if [ $a -lt $b ] 
then
	echo "$a -lt $b: a is less than b"
else
	echo "$a -lt $b: a is not less than b"
fi
	
if [ $a -ge $b ]
then
	echo "$a -ge $b: a is greater or equal to b"
else
	echo "$a -ge $b: a is not greater or equal to b"
fi
	
if [ $a -le $b ]
then
	echo "$a -le $b: a is less or equal to b"
else
	echo "$a -le $b: a is not less or equal to b"
fi
```	

- 布尔运算符
	
运算符|	说明|	举例
------|-----|------
!	 |非运算	表达式为true 则返回false,否则返回true|	[ ! false ]
-o 	 |或运算	有一个表达式为true，则返回true|	[ $a -lt 20 -o $b -gt 100 ]
-a	 |与运算	两个表达式都为true 才返回true|	[ $a -lt 20 -a $b -gt 100]

```shell
#!/bin/bash

a=20
b=10

if [ $a -lt 20 -o $b -gt 10 ]
then
	echo "$a<20 or $b>10"
else
	echo "$a >= 20 or $b <= 10"
fi
```

- 字符串运算符
	
运算符|	说明|	举例
------|-----|------
=	|检测两个字符串是否相等,相等返回 true| [ $a = $b ] 返回 false。
!=	|检测两个字符串是否相等,不相等返回 true|	[ $a != $b ] 返回 true。
-z	|检测字符串长度是否为0,为0返回 true|	[ -z $a ] 返回 false。
-n	|检测字符串长度是否为0,不为0返回 true|	[ -n $a ] 返回 true。
str |检测字符串是否为空,不为空返回 true| [ $a ] 返回 true

```shell
#!/bin/bash

a="abc"
b="efg"

if [ $a = $b ]
then
	echo "a = b"
else
	echo "a != b"
fi

if [ -z $a ]
then
	echo "-z $a: 字符串长度为0"
else
	echo "-z $a: 字符串长度不为0"
fi

if [ $a ]
then
	echo "$a: 字符串为空串"
else
	echo "字符串不为空"
fi
```

- 文件测试运算符
	
运算符|	说明|	举例
------|-----|------
-b file	|检测文件是否是块设备文件,如果是,则返回 true|	[ -b $file ] 返回 false。
-c file	|检测文件是否是字符设备文件,如果是,则返回 true|	[ -b $file ] 返回 fals e。
-d file |检测文件是否是目录,如果是,则返回 true|	[ -d $file ] 返回 fals e。
-f file	|检测文件是否是普通文件(既不是目录,也不是设备文件),如果是,则返回 t rue|	[ -f $file ] 返回 true。
-g file	|检测文件是否设置了 SGID 位,如果是,则返回 true|[ -g $file ] 返回 false。
-k file	|检测文件是否设置了粘着位(Sticky Bit),如果是,则返回 true|	[ -k $file ] 返回 false。
-p file	|检测文件是否是具名管道,如果是,则返回 true|[ -p $file ] 返回 false。
-u file	|检测文件是否设置了 SUID 位,如果是,则返回 true|[ -u $file ] 返回 false。
-r file	|检测文件是否可读,如果是,则返回 true|[ -r $file ] 返回 true。
-w file	|检测文件是否可写,如果是,则返回 true|[ -w $file ] 返回 true。
-x file	|检测文件是否可执行,如果是,则返回 true|[ -x $file ] 返回 true。
-s file	|检测文件是否为空(文件大小是否大于0),不为空返回 true|[ -s $file ] 返回 true。
-e file |检测文件(包括目录)是否存在,如果是,则返回 true| [ -e $file ] 返回 true 。

```shell
#!/bin/bash

file="/Users/lena/developer/LearnShell/README.md"

if [ -r $file ]
then
	echo "文件有可读权限"
else
	echo "文件不可读"
fi
```

##### 注释
shell 没有多行注释，只有单行注释，在需要注释的行首加上 # 号即可 

<center>[上一节](../len02)　　　　　　　　　　[下一节](../len04)</center>
