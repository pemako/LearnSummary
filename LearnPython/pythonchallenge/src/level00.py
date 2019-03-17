# -*- coding:utf-8 -*-
# 2019/03/16 16:26:00

'''
url: http://www.pythonchallenge.com/pc/def/0.html
Hint: try to change the URL address. 要想进入下一题，需要改变URL地址

除了提示只有一张图片上包含信息，下一题的URL可能就隐藏在图片中。故根据
图片上的 238可以知道 2**38=274877906944.0 是否就是修改 
0.html -> 274877906944.0.html  -》 访问无该地址 猜想是否需要一个整数
故 274877906944.0.html -> 274877906944.html 进入下一关。

Python Challenge 的所有关卡都是采用这种解题的方式进入下一关。本题为示例
'''

if __name__ == '__main__':
    import math
    print(math.pow(2, 38))  # 274877906944.0
