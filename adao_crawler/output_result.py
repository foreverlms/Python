#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/26 22:58
"""

import os

def write_md(biscuits={},comments={}) :
    comment_dict=dict(zip(biscuits,comments))
    with open('README.md','a',encoding='utf-8') as f :
        for biscuit,comment in comment_dict.items() :
            f.write('#### '+biscuit)
            f.write('\n')
            f.write(comment.encode('utf-8').decode('utf-8'))
            f.write('\n')