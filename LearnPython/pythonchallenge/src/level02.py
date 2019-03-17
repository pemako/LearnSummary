# -*- coding:utf-8 -*-
# 2019/03/16 18:36:00

'''
url: http://www.pythonchallenge.com/pc/def/ocr.html 根据提示信息可能在源码文件中
打开页面源码发现一行注释 <!--find rare characters in the mess below:--> 及下面的
混乱源码，大致看了基本上是特殊字符的集合!@#$%^&*()_+{}[] 

我这边的解题思路，把这些特殊的字符全部去掉后看看还有什么内容，遍历所有字符串，查
看下除了特殊字符外还有那些内容

{'\n': 1221, 
'%': 6104, 
'$': 6046, 
'@': 6157, 
'_': 6112, 
'^': 6030, 
'#': 6115, 
')': 6186, 
'&': 6043, 
'!': 6079,
'+': 6066, 
']': 6152, 
'*': 6034, 
'}': 6105, 
'[': 6108, 
'(': 6154, 
'{': 6046, 
'e': 1, 
'q': 1, 
'u': 1, 
'a': 1, 
'l': 1, 
'i': 1, 
't': 1, 
'y': 1}

查看结果猜测下一题的页面应该为 equality.html
'''

if __name__ == '__main__':
    import re, urllib.request
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    res = urllib.request.urlopen(url).read().decode('utf-8')
    #text = res.split('-->')[-2].split('<!--')[1]
    text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(res)[-1]
    counts = {}
    for c in text: counts[c] = counts.get(c, 0) + 1
    print(counts)

    # 因此字母的排列顺序
    s = ''.join(re.findall('[a-z]', text))
    print(s)
