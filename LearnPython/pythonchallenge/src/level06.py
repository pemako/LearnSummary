# -*- coding:utf-8 -*-
# 2019/03/16 23:01:00

'''
url: http://www.pythonchallenge.com/pc/def/channel.html

查看页面源码 发现两处注释 一处 <!-- <-- zip -->
还有一处是 <!-- The following has nothing to do with the riddle 
itself. I just thought it would be the right point to offer you
to donate to the Python Challenge project. Any amount will be 
greatly appreciated.

-thesamet
-->

图片上没有任何有用的信息，除了上面的注释源码中也没有找到其余的有效信息
根据作者注释的尿性不是 thesamet 就是 zip
尝试一下发现zip.html是正确的，但是页面的内容仅有 yes. find the zip. 的提示信息

说明直接是zip.html 不对；在分析图片上是一个拉锁半拉开的状态，还有zip的提示；是不是
要说明有一个zip的压缩文件，尝试一下 channel.zip 发现确实存在

解压该文件首先查看readme.txt 中的提示
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
'''

import zipfile
import urllib.request
import io
import re


if __name__ == '__main__':

    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    conts = urllib.request.urlopen(url).read()
    with zipfile.ZipFile(io.BytesIO(conts), 'r') as z:
        filelist = z.namelist()

        def get_contents(p):
            text = z.read('{}.txt'.format(p)).decode('utf-8')
            m = re.match('Next nothing is ([0-9]+)', text)
            if not m:
                print(text)
            return m.group(1)

        zpp = []
        p = 90052
        for i in range(len(filelist)):
            zpp.append(p)
            try:
                p = get_contents(p)
            except:
                pass
        # Collect the comments. 根据提示收集评论信息

        info = b''.join(
            [z.getinfo('{}.txt'.format(p)).comment for p in zpp]).decode()
        print(info)

        '''
        ****************************************************************
        ****************************************************************
        **                                                            **
        **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
        **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
        **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
        **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
        **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
        **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
        **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
        **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
        **                                                            **
        ****************************************************************
         **************************************************************
        '''

        # hockey.html 获取页面内容 it's in the air. look at the letters.
        # 没有明白这句话的意思 最终答案是 oxygen.html
