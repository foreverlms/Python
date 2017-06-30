#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/26 22:48
"""

from download import download
import output_result
import adao_parser
# downloader=download.Html_Downloader()
#初始串号为：https://h.nimingban.com/t/4715940?r=4715940
url='https://h.nimingban.com/t/4715940?r=4715940'
parser=adao_parser.Adao_Parser()
parser.parse(url)
all_comments=parser.all_comments
biscuits=parser.biscuit
# print(len(all_comments))
# print(len(biscuits))
output_result.write_md(biscuits,all_comments)