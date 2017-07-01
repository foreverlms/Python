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

def write_md(biscuits={},comments={}) :
    comment_dict=dict(zip(biscuits,comments))
    with open('README.md','a',encoding='utf-8') as f :
        for biscuit,comment in comment_dict.items() :
            # if comment[:2]=='>>' :
            #     comment=comment.replace('>>','\\>>',1)
            if '>>' in comment :
                comment=comment.replace('>>','\\>>')
            f.write('#### '+biscuit)
            f.write('\n')
            f.write(comment.encode('utf-8').decode('utf-8'))
            f.write('\n')