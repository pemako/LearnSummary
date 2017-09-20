#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 根据给定的年月日以数字形式打印出日期

months = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'Setember',
    'October', 'November', 'December'
]

# 以1 ~ 31的数字作为结尾的列表
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

year = raw_input("Year: ")
month = raw_input("Month（1- 12）：")
day = raw_input("Day(1-31): ")

mouth_number = int(month)
day_number = int(day)

mouth_name = months[mouth_number -1]
day_name = day + endings[day_number - 1]

print mouth_name + ' ' + day_name + ' ' + year
