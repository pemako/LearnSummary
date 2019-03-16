#!/bin/bash

# 定义变量
# - 首个字符必须为数字(a-z, A-Z)
# - 中间不能有空格，可以使用下划线(_)
# - 不能使用标点符号
# - 不能使用bash里面的关键字
your_name="domob"

# 使用
# - 使用一个定义过的变量，只需要在变量名前面加上$ 符号即可
echo $your_name

# - 变量下面使用格式也是合法的
echo ${your_name}

# 重新定义
your_name="zhangsan"
echo $your_name

# 只读变量
# - 只读变量的值不能被修改
readonly my_age=25
echo $my_age

# 打开下行的注释文件会报错 因为 my_age 变量为只读变量不能被修改
#my_age=26

# 删除变量 unset variable_name
# - 变量被删除后不能再次使用，unset命令不能删除只读变量
unset your_name
echo $your_name
