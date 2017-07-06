#! usr/bin/env python3
# coding:utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/26 22:48
"""

from urllib import request

# class Html_Downloader(object) :
#     def __init__(self):
#         pass
def download(url=''):
    if url is None :
        return None
    res_url=request.urlopen(url)
    if res_url.getcode() !=200 :
        return None
    return res_url.read()