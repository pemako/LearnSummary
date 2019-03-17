# -*- coding:utf-8 -*-
# 2019/03/17 10:25:00

'''
url: http://www.pythonchallenge.com/pc/def/integrity.html进入页面源码

title: working hard? 还有一个🐝点击小蜜蜂的时候有充气的效果，看源码最
后面的注释明显是需要提供一个 username 和 password才能进入 good.html.
查看un 和 pw 都是以BZ 开头，猜测是不是bizp2 压缩算法
bee? busy. busy? busy too ? bz2?
'''


if __name__ == '__main__':
    import bz2
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    username = bz2.BZ2Decompressor().decompress(un)
    password = bz2.BZ2Decompressor().decompress(pw)
    print(username, password)
