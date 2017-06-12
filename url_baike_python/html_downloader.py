#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/1 22:59
"""

#利用request实现下载网页
from urllib import request
class HtmlDownloader() :
    def download(self, url):
        if url is None :
            return None
        response=request.urlopen(url)

        if response.getcode() !=200 :
            return None
        return response.read()
