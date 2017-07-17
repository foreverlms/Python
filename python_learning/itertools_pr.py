#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/14 18:41
"""

import itertools
#repeat重复
# cs=itertools.repeat('A',4)
# for n in cs:
#     print(n)
# natuals=itertools.count(1)
# #takewhile截取
# ns=itertools.takewhile(lambda x :x <=10,natuals)
# print(list(ns))
# #chain串联
# for c in itertools.chain('ABC','XYZ') :
#     print(c)
# #groupby把迭代器中相邻重复元素挑出放到一起
# for key,group in itertools.groupby('AAaABBBbbCbCAAA',lambda x : x.upper()) :
#     print(key,list(group))
dic_1={
    'Bio' :1,
    'Bob' :2
}
for key,value in dic_1.items() :
    print(key,value)
print(type(itertools.groupby('AAaABBBbbCbCAAA',lambda x : x.upper())))
print(dict(itertools.groupby('AAaABBBbbCbCAAA',lambda x : x.upper())))
