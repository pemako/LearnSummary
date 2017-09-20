##### shell 数组

- 概述
 - bash 支持一维数组（不支持多维数组），并且没有限定数组的大小。数组元素下标由0开始编号
- 定义
 - 在shell中，用括号来表示数组，数组元素用"空格"符号分隔开。定义数组的形式有如下两种
```shell
array=(value1 value2 .. valuen)
或
array=(
value0
value1
value3
)
```

- 数组读取
 - 读取数组元素值得一般格式是`${array[index]}`
 - 使用@或*可以获取数组中的所有元素 `${array[@] 或 ${array[*]}`

- 获取数组元素的长度 
 - 获取数组长度的方法和获取字符串长度的方法相同
```shell
# 获取数组元素的个数
length=${array[@]}
# 或者
length-$array[*]
# 取得数组单个元素的长度
lengthn=${#array[n]}
```
<center>[上一节](../len04)　　　　　　　　　　[下一节](../len06)</center>
