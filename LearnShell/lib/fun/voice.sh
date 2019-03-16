#!/usr/bin/env bash
# @create 17/03/22 21:37:47
# @author pemakoa@gmail.com

while [ 1 ]
do
    sleep $((($RANDOM % 10) * 100))
    osascript -e "set Volume 2" # 主动设置音量打下
    say hello
    osascript -e "set Volume 0" # 最后让电脑消音
done

