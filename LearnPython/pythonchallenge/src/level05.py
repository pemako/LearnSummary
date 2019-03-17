# -*- coding:utf-8 -*-
# 2019/03/16 20:40:00

'''
url: http://www.pythonchallenge.com/pc/def/peak.html -> 查看页面源码 提示
-> http://www.pythonchallenge.com/pc/def/banner.p 猜测需要转换成声音获取下
一关的地址。  发现这个思路行不通，最后查了相关的资料才知道这个题目是其实是
考察Python内置的 pickle 模块，提示信息 'peak hell sounds familiar' 其实就是
说 peak -> pickle

-虽然解出来但是全是列表，看不明白意图是啥？ 最后只能求助于网络解决

作者的脑洞真大🤦‍♂️

获取下一题的答案 channel.html
'''

if __name__ == '__main__':
    import pickle
    import urllib.request
    banner = 'http://www.pythonchallenge.com/pc/def/banner.p'
    res = urllib.request.urlopen(banner).read()
    banner = pickle.loads(res)

    for line in banner:
        print(''.join(temp[0] * temp[1] for temp in line))
