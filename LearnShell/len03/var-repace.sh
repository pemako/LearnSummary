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

