##### echo 命令 & printf

###### echo 命令
- 显示转义字符
```shell
echo "\"It is a test\""
# 输出 "It is a test" 双引号可以省略 如：\"It is a test\"
```
- 显示变量
```shell
name="Domob"
echo "$name it is a test"
# 输出 Domob it is a test 同样双引号可以省略

# 如果变量与其它字符相连接的话，需要使用大括号（{}）
mouth=4
echo "${mouth}-07-2016" 
# 输出 4-0702016
```
- 显示换行符
```shell
echo "Ok!\n"
echo "It is a test"
# 输出
# Ok!
# It is a test
```
- 显示不换行
```shell
echo "Ok!\c"
echo "It is a test"
# 输出 Ok!It is a test
```
- 显示结果重定向到文件
```shell
echo "It is a test data" > filename
```
- 原样输出字符串
```shell
# 如需要原样输出字符串（不进行转义），请使用单引号
echo '$name'
```
- 显示命令执行结果
```shell
echo `date`
```

- 总结
 - 双引号可有可无
 - 单引号主要用在原样输出中
 - `` 显示的是执行的结果
 - \n 换行 \c 不换行
 - 变量和其它字符相连需要使用大括号

###### printf 命令
```shell
#!/bin/bash

# 格式化字符串为双引号
printf "%d %s\n" 1 "abc"

# 单引号和双引号效果一样
printf '%d %s\n' 1 "abc"

# 没有引号也可以输出
printf %s domob

# 格式只指定一个参数，但多处的参数仍然会按照格式输出，format-string 被重用
printf %s domob developer
printf "%s\n" domob developer

# 如果没有 arguments,那么 %s 用 NULL 代替,%d 用0代替
printf "%s and %d \n"

# 如果以 %d 的格式来显示字符串,那么会有警告,提示无效的数字,此时默认置为0
printf "The first program always prints'%s,%d\n'" Hello Shell

```
<center>[上一节](../len05)　　　　　　　　　　[下一节](../len07)</center>
