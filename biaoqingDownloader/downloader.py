#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
# @Date    : 2018-04-20 13:15:38
# @Author  : Bob Liao (codechaser@163.com)
# @Link    : https://github.com/coderchaser


import os
import time
import argparse
import requests
import random
import json
import threading
# from decorator import downloader_logger

# code 0 represents https://www.doutula.com/apidoc
API_URL_DICT={0:"https://www.doutula.com/api/search?keyword={keyword}&mime={image_type}&page={page}"}
#random choice from these user agents
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'), )

class Downloader(object) :
    def __init__(self,number,keyword,image_type,filepath,verbose,api_code=0) :
        #TODO: self.__image_url_list defined as queue instead of list to support multi thread downloading
        self.__image_url_list = []
        #a list for storing image urls
        self.__number = number
        #the number of images to be downloaded
        self.__api_code = api_code
        #which site's api to choose. Currently only one.
        self.__keyword = keyword
        #keywords of the images
        self.__image_type = image_type
        #image type 0 :all kinds 1:GIF 2:static images
        self.__filepath = filepath
        #where to store those images
        self.__verbose = verbose
        #enable the verbose info?
    def __get_image_url(self) :
        for i in range(1,51) :
            api_url=API_URL_DICT[self.__api_code].format(keyword=self.__keyword,image_type=self.__image_type,page=i)
            try:
                rq=requests.get(api_url,headers={'User-Agent':random.choice(USER_AGENTS)},timeout=5)
                response_dict=rq.json()
                self.__image_url_list.extend([entry['image_url'] for entry in response_dict['data']['list']])
                #TODO: Can i use multi threads here? This is a kind of IO-intenseive work ?
                if len(self.__image_url_list) >= self.__number:
                    break
                if response_dict['data']['more'] != 1:
                    break;
            except requests.ConnectionError as e:
                print(e)
            finally :
                rq.close()# close exsists?

    def __download(self):
        self.__get_image_url()
        print('Now downloading images from https://www.doutula.com ...')
        if not os.path.exists(self.__filepath):
            os.makedirs(self.__filepath)
        for i in range(self.__number) :
            image_url=self.__image_url_list[i]
            if self.__verbose :
                print("Dwonload images: {}".format(image_url))
            extension='.'+image_url.split('.')[-1]
            try:
                filename=os.path.join(self.__filepath,'{0}{1}'.format(self.__keyword,i)+extension)
                # self.image_download(filename,image_url)
                download_rq=requests.get(image_url)
                with open(filename,'wb') as f :
                    f.write(download_rq.content)
            except Exception as e:
                print(e)
            time.sleep(1)
        print("Images about {} have been downloaded.".format(self.__keyword))
    def run(self) :
        self.__download()

    # @downloader_logger
    # def image_download(self,filename,image_url):
    #     download_rq=requests.get(image_url)
    #     with open(filename,'wb') as f :
    #                 f.write(download_rq.content)


def get_parser() :
    parser = argparse.ArgumentParser(description="download interesting emoj images from www.doutula.com via command line")
    parser.add_argument('keywords',metavar='KEYWORD',type=str,nargs='*',
        help='the keywords to be searched')
    parser.add_argument('-t','--type',type=int,default=0,choices=range(0,3),
        help='choose image type to be downloaded. 0 represents all, 1 represents GIF , 2 represents static image')
    parser.add_argument('-n','--num',type=int,default=50,
        help='number of images to be downloaded')
    parser.add_argument('-c','--clear',action='store_true',
        help='enable clear the log file')
    parser.add_argument('-d','--dir',type=str,
        help='where to store the images, default is ./tmp/keyword/')
    parser.add_argument('-v','--verbose',action='store_true',
        help='enable show the whole downloading info')

    return parser

def download(**kwargs):
    for keyword in kwargs['keywords'] :
        if kwargs['dir'] :
            dirpath=kwargs['dir']+"/"+keyword
        else :
            dirpath='./tmp/'+keyword
        print(dirpath)
        downloader=Downloader(kwargs['num'],keyword,kwargs['type'],dirpath,kwargs['verbose'])
        downloader.run()

def command_line_runner():
    parser=get_parser()
    kwargs=vars(parser.parse_args())

    if kwargs['clear']:
        with open('./biaoqingDownloader.log','w') as f:
            f.truncate()

    if not kwargs['keywords']:
        #if no keywords assigned, return with help info
        parser.print_help()
        return

    download(**kwargs)



if __name__ == '__main__':

    ###
    #test this downloader
    ###
    # downloader=Downloader(20,'金馆长',0,'./tmp',false)
    # downloader.run()
    command_line_runner()
