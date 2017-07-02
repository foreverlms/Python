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

import matplotlib.pyplot as plt

def write_md(biscuits={},comments={}) :
    #将爬取到的所有评论写入md格式文件
    comment_dict=dict(zip(biscuits,comments))
    with open('./warning_result/README.md','a',encoding='utf-8') as f :
        f.write('## All comments are hrer.Images are not included.')
        f.write('\n')
        for biscuit,comment in comment_dict.items() :
            if '>>' in comment :
                #由于markdown语法中双>>表示双竖线，我们需要将其转义
                comment=comment.replace('>>','\\>>')
            #以饼干为小标题
            f.write('#### '+biscuit)
            f.write('\n')
            #评论内容
            f.write(comment.encode('utf-8').decode('utf-8'))
            f.write('\n')

def chart_output(words=[]):
    data=[word[1] for word in words]
    label=[word[0] for word in words]
    plt.bar(range(len(data)),data,tick_label=label)
    plt.show()

def word_cloud() :
    pass