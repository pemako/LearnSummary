#!/usr/env ruby -w
# -*- coding: utf-8 -*-

# Ruby 数据类型
# Ruby支持的数据类型包括基本的Number, String, Ranges, Symbols, true, false和nil这几个
# 特殊值，同时还有两个重要的数据结构 Array 和 Hash

# 1. Number
# 整型分为两种，如果在31位以内那么为Fixnum.如果超过则为Bignum实例
# 在整数前面加一个可选的前导符号（0对应octal, 0x -> hex, 0b->binary）,后面跟一串数字
# !!下划线字符在数字字符串中被忽略
# !!可以获取一个ASCII 字符或一个用问号标记的转义序列的整数值
puts 123
puts 1_234 # 1234
puts 0377  # 225
puts 0xff  # 225
puts 0b1011 # 11
puts "a".ord  # 97
puts ?\n  #

# Integer 整型字面量
a1=0
a2 = 1_000_000 # 带千分位的整型
a3 = 0xa
puts a1, a2, a3

# 2. 浮点数 Float
# 3. 算数操作 +-*/ 指数**(不必是整数)
# 4. 字符串类型
# Ruby 的字符串是一个8位字节序列，他们是类String的对象
# 双引号标记的字符串允许替换和使用反斜线符号，单引号标记的字符串不允许替换，且只允
# 许使用 \\ 和 \' 两个反斜线符号

puts 'escape using "\\"'; # escape using "\"
puts 'That\'s right'       # That's right


# 5. 数组
=begin
数组字面量通过[]中以逗号分隔定义，且支持range定义
1). 数组通过[] 索引访问
2). 通过赋值操作插入，删除，替换元素
3). 通过+,-号进行合并和删除元素，且集合作为新集合出现
4). 通过<<号向原数据追加元素
5). 通过*号重复数组元素
6). 通过 | 和 & 符号做并集和交集操作
=end

ary = ["fred", 10, 3.14, "That is a string", "Last element"]
ary.each do |i|
    puts i
end

# 6. Hash 类型
# 哈希是在大括号内放置一系列键/值对，键和值之间使用逗号和序列 => 分隔。尾部的逗号会被忽略

hsh = colors = {"red"=>0xf00, "green"=>0x0f0, "blue"=>0x00f}
hsh.each do |key, value|
    print key, " is ", value, "\n"
end

# 7. 范围类型
# 范围是通过设置一个开始值和一个结束值来表示。范围可使用 s..e(包含结束值) 和 s...e(不包含
# 结束值) 来构造，或者通过 Range.new 来构造 。
# 当作为一个迭代器使用时，范围会返回序列中的每个值

(10..15).each do |i|
    print i, ' '
end
