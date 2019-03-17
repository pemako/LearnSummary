# -*- coding:utf-8 -*-
# 2019/03/16 16:27:00

'''
URL http://www.pythonchallenge.com/pc/def/274877906944.html 跳转到地址
http://www.pythonchallenge.com/pc/def/map.html

根据左下角的建议信息
- 使用提示，大多数情况下他们是有帮助的
- 研究给到的数据
- 避免剧透

给到的图片信息是 k->m  o->q  e->g 还有给到的一串红色的加密提示信息"
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm 
jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

解出加密字符串提示的内容既可以知道通往下一题的答案。再根据图片信息可以
知道加密规则是进行字符串替换 k->m o->q e->g 观察规律可以知道每个字幕
向后移动两位可以知道加密的字母替换规则如下。这种加密方式为凯撒密码
[参考](https://zh.wikipedia.org/wiki/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC)


=> 加密规则 En(x)=(x+n) mod 26  其中n为偏移量
=> 解密规则 Dn(x)=(x-n) mod 26

a b c d e f g h i j k l m n o p q r s t u v w x y z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
c d e f g h i j k l m n o p q r s t u v w x y z a b

a->97

按照对应规则解出加密的提示内容,可以按照最笨的方式一个字母一个字母替换^_^

这里采取字符串移位解决 根据获取到的提示信息
i hope you didnt translate it by hand. thats what computers are for.
doing it in by hand is inefficient and that's why this text is so
long. using string.maketrans() is recommended. now apply on the url.

可以知道 map.html -> ocr.html

则可以知道第二题的地址为 ocr.html

=> 根据提示的内容知道可以采用 string.makertrans()函数可以解决 

=> 注意在Python2 和Python3中的区别
➜  lib git:(master) python
Python 2.7.16 (default, Mar  4 2019, 09:02:22)
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import string
>>> lower = string.lowercase
>>> upper = string.uppercase
>>> letters = string.letters
>>> lower
'abcdefghijklmnopqrstuvwxyz'
>>> upper
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> trans = string.maketrans(lower, lower[2:]+lower[:2])
>>> 'g fmnc wms'.translate(trans)
'i hope you'
>>>
➜  lib git:(master) python3
Python 3.7.2 (default, Feb 12 2019, 08:16:38)
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import string
>>> lower = string.ascii_lowercase
>>> upper = string.ascii_uppercase
>>> letters = string.ascii_letters
>>> trans = str.maketrans(lower, lower[2:]+lower[:2])
>>> 'g fmnc wms'.translate(trans)
'i hope you'
>>>
'''

import string


def caesar_cipher(s, o, f=True):
    '''s 为需要解密的字符串o为加密时候使用的偏移量
    f=True 为解密，f=False 为加密'''
    new_s = ''
    if not f:
        o = -o
    for i in s:
        if i.isalpha():
            if i.isupper():
                i = chr((ord(i) + o - 65) % 26 + 97).upper()
            else:
                i = chr((ord(i) + o - 97) % 26 + 97).lower()
        new_s = new_s + i

    return new_s


def use_built_in_function_with_python3(str, offset, flag=False):
    '''str 需要转化的字符串 offset 对应的偏移量  flag=True 为加密，f=False 为解密'''
    lower_str = string.ascii_lowercase
    super_str = string.ascii_uppercase
    input_str = string.ascii_letters
    output_str = lower_str[offset:] + lower_str[:offset] + \
        super_str[offset:] + super_str[:offset]

    if flag:
        t = str.maketrans(output_str, input_str)
    else:
        t = str.maketrans(input_str, output_str)
    return str.translate(t)


if __name__ == '__main__':
    s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    a = use_built_in_function_with_python3(s, 2)
    print(a)
    print(use_built_in_function_with_python3(a, 2, True))

    print(use_built_in_function_with_python3('map', 2))
