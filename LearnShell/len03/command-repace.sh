#!/bin/bash

# 获取当前的时间并保存到DATE变量中
DATE=`date "+%Y%m%d %H:%M:%S"`
echo $DATE

# 获取当前有多少用户在登陆
USERS=`who | wc -l`
echo $USERS
