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
import re
from urllib.request import urljoin
from bs4 import BeautifulSoup
class HtmlParser() :
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None :
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url, soup):
        new_urls=set()
        #通过正则匹配url
        links=soup.find_all('a',href=re.compile(r'/item/[%/0-9a-zA-Z]+'))
        for link in links :
            new_url=link['href']
            new_full_url=urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        res_data={}
        #<dd class="lemmaWgt-lemmaTitle-title">
        #<h1>Python</h1>
        title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"]=title_node.get_text()
        res_data['url']=page_url
        summary_node=soup.find('div',class_="lemma-summary")
        res_data["summary"]=summary_node.get_text()
        return res_data
