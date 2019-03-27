# -*- coding:utf-8 -*-
# 2019/03/18 21:02:00

'''
url: http://www.pythonchallenge.com/pc/return/evil.html 查看页面源码提示信息

dealing evil 后面有一个evil1.jpg 的图片，尝试会不会存在 evil2.jpg 查看果然有；且图
片上的信息为 Not jpg .gfx 是不是告诉我们还有一个 evil2.gfx 的文件。访问确实存在一该
文件；继续访问evil3.jpg 看看是否有更多的线索信息，看到的提示信息 no more evils...,
继续访问 evil4.jpg 返回的不是一个图片信息但是该文件存在的，访问evil5.jpg 提示无该文件

说明需要的信息就存在 evil2.gfx， evil4.jpg 文件中，现在只要能解析该文件应该可以找到正
确答案。 

1、先读取evil4.jpg 的内容  # Bert is evil! go back!
2、在读取 evil2.gfx 的内容
'''

def read_file_info(_f):
	with open(_f) as f:
		return f.read()

if __name__ == '__main__':
	evil4 = read_file_info('../data/evil4.jpg')
	# fgx = read_file_info('../data/evil2.gfx')