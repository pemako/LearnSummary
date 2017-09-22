#!/usr/bin/ruby
# -*- coding:utf-8 -*-

# Ruby 支持五种类型的变量。
# 1. 一般小写字母、下划线开头：变量（Variable）。
# 2. $开头：全局变量（Global variable）。
# 3. @开头：实例变量（Instance variable）。
# 4. @@开头：类变量（Class variable）类变量被共享在整个继承链中
# 5. 大写字母开头：常数（Constant

$global_variable = 10
class Class1
	def print_global()
		puts "全局变量在Class1 中输出为 #$global_variable"
	end
end

class Class2
	def print_global()
		puts "全局变量在Class2 中输出为 #$global_variable"
	end
end

Class1.new.print_global
Class2.new.print_global

puts __FILE__, __LINE__
