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

import jieba.posseg as pseg
from collections import Counter
class Jieba_Analyser() :
    def __init__(self,all_comments,biscuits):
        #分词列表
        self.words_list=[]
        #全部词语
        self.full_words_list=[]
        #词频最高的词数列表
        self.most_words_list=[]
        #最长评论
        self.longest_comment=''
        #所有评论与对应饼干形成的字典
        self.comments=dict(zip(biscuits,all_comments))
    def analyse(self):
        for comment in self.comments.values() :
            jieba_words=pseg.cut(comment)
            for word in jieba_words :
                #为了筛选无意义词，只收集词性属于n与l的词。
                #由于’神父‘一词为主串引导的词，不予考虑
                if len(word.word)>=2 and not word.word=='神父' and word.flag=='n' or word.flag=='l' :
                    self.words_list.append(word.word)
                if len(word.word)>=2 and not word.word=='神父':
                    self.full_words_list.append(word.word)
        #统计频率最高的10个词
        self.most_words_list=self._get_most_words(10)
        self.longest_comment=self._get_longest_commont(self.comments.values()).encode('utf-8').decode('utf-8')
    def _get_most_words(self,num):
        #统计词频最高的num个词
        counter_words=Counter(self.words_list)
        return counter_words.most_common(num)
    def _get_longest_commont(self,comments):
        #筛选长度最长的评论
        return max(comments,key=lambda x :len(x))
    # def _get_full_most_words(self,num):
    #     #统计所有词语词频最高的num个词。
    #     counter_words=Counter(self.full_words_list)
    #     return counter_words.most_common(num)