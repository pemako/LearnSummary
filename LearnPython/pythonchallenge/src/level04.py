# -*- coding:utf-8 -*-
# 2019/03/16 20:00:00

'''
url: http://www.pythonchallenge.com/pc/def/linkedlist.html 访问该页面提示 linkedlist.php

-> 访问 linkedlist.php 发现除了一张图片啥也没有，看来作者喜欢把题目隐藏在页面源码中
查看页面源码返现 对应的提示信息 <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it 
will never end. 400 times is more than enough. --> 及 一个URL=linkedlist.php?nothing=12345
访问页面获取页面信息 为44827 替换nothing的参数发现可以继续访问

根据提示作者的意图是循环400次获取下一题的题目。 最终获取 peak.html
'''


def get_num_from_content(nothing):
    import re
    import urllib.request
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(
        nothing)
    res = urllib.request.urlopen(url).read().decode('utf-8')
    m = re.match('and the next nothing is ([0-9]+)', res)
    if not m:
        print(res)
        return

    return m.group(1)


if __name__ == '__main__':
    p = 12345
    for i in range(400):
        p = get_num_from_content(p)
