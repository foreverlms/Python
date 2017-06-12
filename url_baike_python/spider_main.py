#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/1 22:58
"""

import url_manager, html_downloader, html_parser, html_outputer

class SpideMain() :
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        count=1
        while self.urls.has_new_url() :
            try:
                    new_url=self.urls.get_new_url()
                    html_cont=self.downloader.download(new_url)
                    print("Crawing the %d URL: %s" %(count,new_url))
                    new_urls,new_data=self.parser.parse(new_url,html_cont)
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)
                    #设定爬取url数量
                    if count==100 :
                        print("Craw finished.")
                        break
                    count+=1
            except :
                print('\033[1;31;40m')
                print("Craw failed")
                print('\033[0m')

        self.outputer.output_html()

if __name__=="__main__" :
    root_url="http://baike.baidu.com/item/Python"
    obj_spider=SpideMain()
    obj_spider.craw(root_url)
