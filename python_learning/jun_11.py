#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/11 16:24
"""
import struct
n=100
n_bit=(n & 0xff000000)
print(n_bit)
print(struct.pack('>I',n))
print(struct.pack('>H',30))
print(struct.pack('>H',45))
print(30&0)