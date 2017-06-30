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
import re
from download import download
from urllib.request import urljoin
from bs4 import BeautifulSoup
from bs4 import element

class Adao_Parser(object) :
    def __init__(self):
        # self.first_url=url
        self.all_comments=[]
        self.biscuit=[]
        self.flag=True
    def parse(self,page_url) :
        html_cont=download(page_url)
        if page_url is None or html_cont is None :
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        while self.flag :
            self._get_comment(page_url,soup)
            # print(self.all_comments)
            if soup.find('span',text='下一页') :
                self.flag=False
                break
            print(page_url)
            # print(self.flag)
            page_url=self._get_next_page(page_url,soup)
            self.parse(page_url)


    def _get_next_page(self,page_url,soup):
        if soup.find('a',text='下一页') :
            next_page = soup.find('a', text='下一页')
            next_page_url = urljoin(page_url, next_page['href'])
            return next_page_url
        else:
            return False

    def _get_comment(self,page_url,soup):
        coments=soup.find_all('div',{'data-threads-id' :re.compile(r'\d+'),'class' : 'h-threads-item-reply'})
        try:
            for comment in coments:
                for element_consist in comment.next_elements:
                    if isinstance(element_consist, element.Tag) and element_consist.name == 'div' and \
                                    element_consist['class'][0] == 'h-threads-content':
                        self.all_comments.append(element_consist.getText().strip().strip())
                    if isinstance(element_consist,element.Tag) and element_consist.name=='span' and \
                                    element_consist['class'][0]=='h-threads-info-uid':
                        self.biscuit.append(element_consist.getText().strip('ID:'))
        except KeyError :
            pass