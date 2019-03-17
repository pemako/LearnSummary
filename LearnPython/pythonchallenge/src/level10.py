# -*- coding:utf-8 -*-
# 2019/03/17 12:28:00

'''
url: http://www.pythonchallenge.com/pc/return/bull.html  查看页面源码
提示：what are you looking at? 页面中有一个 sequence.txt 打开该文件
a = [1, 11, 21, 1211, 111221, 缺省的数列，结合页面中的 len(a[30]) =?
只需找出规律即可解决该题。思路对了但是规律没有找到，查询后发现这个数列
被称为描述数列（Descriptive Sequence）或 自描数列（Self-descriptive-Se
quence）或语言数列（Look And Say Sequence）.简单来说就是后一项是对前一
项的说明下面举几个例子

第一项为 1
第二项为 11 （描述第一项为一个一）
第三项为 21 （描述第二项为二个一）
第四项为 1211 （描述第三项为一个二一个一）
第五项为 11 12 21 （描述第四项为一个一 一个二  两个一）
.....


[参考1] https://oeis.org/A005150
[参考2] https://oeis.org/A005341
[参考3] http://www.geocities.ws/goodprimes/ODescriptive.html
'''


def A005150(n):
    p = "1"
    seq = [1]
    while (n > 1):
        q = ''
        idx = 0
        l = len(p)
        while idx < l:
            start = idx
            idx = idx + 1
            while idx < l and p[idx] == p[start]:
                idx = idx + 1
            q = q + str(idx - start) + p[start]
        n, p = n - 1, q
        seq.append(int(p))
    return seq


def lookandsay(limit, sequence=1):
    import re
    if limit > 1:
        return lookandsay(limit - 1, "".join([str(len(match.group())) + match.group()[0] for matchNum, match in enumerate(re.finditer(r"(\w)\1*", str(sequence)))]))
    return sequence


if __name__ == '__main__':
    r = len(lookandsay(31))
    print(r)  # 5808
