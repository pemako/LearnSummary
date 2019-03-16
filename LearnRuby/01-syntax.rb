#!/usr/env ruby -w
# -*- coding: utf-8 -*-

# Ruby代码中的空白字符，如空格和制表符一般会被胡洛，除非当他们出现在字符串
# 中时才不会被忽略。然而有时候他们用于解释模凌两可的语句。启用-w选项时，这
# 中解释会产生警告

# a + b 被解释为 a+b 这是一个局部变量
# a +b 被解释为 a(+b) 这是一个方法调用

# Ruby 程序中的行尾
# Ruby 把分号和换行符解释为语句的结尾。如果Ruby在行尾遇到运算符，比如+,-
# 或反斜线，他们表示一个语句的延续

# Ruby 标识符
# 标识符是变量、敞亮和方法的名称。Ruby标识符是大小写敏感的。标识符的名字
# 以字母，数字或下划线

# 保留字
# BEGIN do next then END else nil true alias elsif not undef
# and end or unless begin ensure redo until break false rescue
# when case for retry while class if return def in self 
# __FILE__ __LINE__ super module defined?

# Ruby 中的Here Document
# 在 << 之后，指定一个字符串或标识符来终止字符串，并且当前行之后到终止符
# 为止的所有行时字符串的值。
# 如果终止符用引号括起，引号的类型决定过了面向行的字符串类型。注意<<和终
# 止符之间不能有空格

print <<EOF
    这是第一种方式创建here document.
EOF

print <<"EOF"
    这是第二种方式创建here document.
    这是多行字符串
EOF

print <<`EOC`   # 执行命令
    echo hi there
    echo lo there
EOC

print <<"foo", <<"bar" # 进行堆叠
    I said foo.
foo
    I said bar.
bar


# Ruby BEGIN 
# BEGIN { code } 声明code会在程序运行之前被调用

puts "这是主 Ruby 程序"
BEGIN {
    puts "初始化 Ruby 程序"
}

# Ruby END 语句
# END { code } 声明code会在程序的结尾被调用
END {
    puts "这一行代码会最后运行"
}

# Ruby 的注释 可以类似这种单行注释
# 也可以类似下面的进行多行注释
=begin
这里面的都是注释内容
这里也是注释
=end

