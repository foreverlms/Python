#! usr/bin/env python3
# coding =utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/26 22:48
"""

import output_result
import adao_parser
import jieba_analysis

if __name__=='__main__' :
    # 初始串号为：https://h.nimingban.com/t/4715940?r=4715940
    url = 'https://h.nimingban.com/t/4715940?r=4715940'
    #解析
    parser = adao_parser.Adao_Parser()
    parser.parse(url)
    all_comments = parser.all_comments
    biscuits = parser.biscuit
    analyser = jieba_analysis.Jieba_Analyser(all_comments, biscuits)
    analyser.analyse()
    #输出
    output_result.write_md(biscuits, all_comments)
    output_result.chart_output(analyser.most_words_list)
    output_result.word_cloud_output(analyser.full_words_list)