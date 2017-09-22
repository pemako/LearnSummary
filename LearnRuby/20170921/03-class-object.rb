#!/usr/bin/ruby
# -*- coding:utf-8 -*-

# Ruby 类和对象
# Ruby 类中的变量
# 1. 局部变量：在方法中定义的变量。方法外不可用。以小写字母或_开始
# 2. 实例变量: 实例变量可以跨任何特定的实例或对象中的方法使用。实例变量
#       可以从对象到对象的改变。实例变量是在变量名前放置符号 @
# 3. 类变量：类变量可以跨不同的对象使用，类变量属于类，且是类的一个属性
#       类变量在变量名之前放置符号 @@
# 4. 全局变量: 类变量不能跨类使用，如果想要有一个可以跨类使用的变量，需
#       要定义全局变量。全局变量总是以美元符号 $ 开始


class Customer
    @@no_of_customers = 0   # 类变量判断被创建对象数列，确定客户数量
    def initialize(id, name, addr)
        @cust_id = id
        @cust_name = name
        @cust_addr = addr
    end

    def display_details()
        puts "Customer id #@cust_id"
        puts "Customer name #@cust_name"
        puts "Customer addr #@cust_addr"
    end

    def total_no_of_customeers()
        @@no_of_customers += 1
        puts "Total number of customers: #@@no_of_customers"
    end
end

# Ruby 中使用 new 方法创建对象
cust1 = Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
cust2 = Customer.new("2", "Poul", "New Empire road, Khandala")

# 调用方法
cust1.display_details()
cust1.total_no_of_customeers()

cust2.display_details()
cust2.total_no_of_customeers()

=begin
Output:
Customer id 1
Customer name John
Customer addr Wisdom Apartments, Ludhiya
Total number of customers: 1
Customer id 2
Customer name Poul
Customer addr New Empire road, Khandala
Total number of customers: 2
=end
