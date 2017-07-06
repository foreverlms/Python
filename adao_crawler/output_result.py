#! usr/bin/env python3
# coding:utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/26 22:58
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

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
    #生成词频柱状图
    data=[word[1] for word in words]
    label=[word[0] for word in words]
    plt.figure(1)
    plt.legend(('词频',))
    plt.bar(range(len(data)),data,tick_label=label)
    plt.title('评论中词频最高的10个词组')
    plt.savefig('zhuzhuangtu.png')

def word_cloud_output(words=[]) :
    #生成图云
    #Problems to be resolved:
    #It seems that wordcloud receive some certain png file as mask.
    #Some png files may fail to be a mask,I should check it next time.
    d=os.path.dirname(__file__)
    #以Tree.png为mask，也不怎么好看。
    mask_figure_1=np.array(Image.open(os.path.join(d,'Tree.png')))
    #以heart.png为mask，有问题。
    mask_figure_2=np.array(Image.open(os.path.join(d,'heart.png')))
    text=' '.join(words)
    wc_1=WordCloud(background_color='white',font_path=r'C:\Windows\Fonts\等线\Deng.ttf',mask=mask_figure_1)
    wc_1.generate(text)
    wc_1.to_file('word_cloud_1.png')
    wc_2 = WordCloud(background_color='white', font_path=r'C:\Windows\Fonts\等线\Deng.ttf', mask=mask_figure_2)
    wc_2.generate(text)
    wc_2.to_file('word_cloud_2.png')

