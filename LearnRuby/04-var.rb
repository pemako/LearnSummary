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

# Ruby 实例变量
# 实例变量是以@开头，未初始化的示例变量的值为 nil,在使用 -w选项后，会产生警告

class Customer
    def initialize(id, name, addr)
        @cust_id = id
        @cust_name = name
        @cust_addr = addr
    end
    def display_details()
        puts "Customer id #@cust_id"
        puts "Customer name #@cust_name"
        puts "Customer address #@cust_addr"
    end
end

# 创建对象
cust1 = Customer.new("1","John","Wisdom Apartments, Ludhiya")
cust2 = Customer.new("2","Poul","New Empire road, Khandala")

# 调用方法
cust1.display_details()
cust2.display_details()


# Ruby 类变量
# 类变量以 @@开头，且必须初始化后才能在方法定义中使用
# 引用一个为初始换的变量会产生错误。类变量在定义它的类或模块的子类中可以共享使用
# 在使用 -w 选项后，重载类变量会产生警告

class Customer1
    @@no_of_customers = 0
    def initialize(id, name, addr)
        @cust_id = id
        @cust_name = name
        @cust_addr = addr
    end
    def display_details()
        puts "Customer id #@cust_id"
        puts "Customer name #@cust_name"
        puts "Customer address #@cust_addr"
    end

    def total_no_of_customers()
        @@no_of_customers += 1
        puts "Total number of customers: #@@no_of_customers"
    end
end

# 创建对象
cust3 = Customer1.new("1","John","Wisdom Apartments, Ludhiya")
cust4 = Customer1.new("2","Poul","New Empire road, Khandala")
# 调用方法
cust3.total_no_of_customers()
cust4.total_no_of_customers()


# Ruby 常量
# 常量以大写字母开头。定义在类或模块内的常量可以从类或模块的内部访问，定义在类或模
# 块外的常量可以被全局访问。常量不能定义在方法内。引用一个未初始化的常量会产生错误。
# 对已经初始化的常量赋值会产生警告。

class Example
    VAR1 = 100
    VAR2 = 200
    def show
        puts "第一个常量的值为  #{VAR1}"
        puts "第二个常量的值为  #{VAR2}"
    end
end

# 创建对象
object = Example.new()
object.show


# Ruby 的伪变量
# self 当前方法的接收器对象
# true 代表 true 的值
# false 代表 false 的值
# nil代表 undefined 的值
# __FILE__ 当前源文件的名称
# __LINE__ 当前行在源文件汇总的编号
