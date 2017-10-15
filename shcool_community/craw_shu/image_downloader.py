#! usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date    : 2017/9/30 15:42
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser

import requests
import time
from requests.exceptions import Timeout
from PIL import Image
from io import BytesIO
class Image_Downloader(object) :
    def __init__(self):
        pass
    @staticmethod
    def download(image_url,number,fontname):
        '''
        :param image_url: 从教务处获取验证码的网址
        :param number: 下载验证码数量
        :return: 下载的图片存放于./test_data文件夹中
        '''
        for i in range(number) :
            try :
                res=requests.get(image_url,timeout=5)
                image_bytes=BytesIO(res.content)
                image=Image.open(image_bytes)
                image.save('./testdata/eng.{}.exp{}.jpg'.format(fontname,i))
                print('Downloading {} pictures'.format(i))
                time.sleep(1)
            except Timeout as e :
                print('Timeout error!')
if __name__=='__main__' :
    # Image_Downloader.download('http://cj.shu.edu.cn/User/GetValidateCode?%20%20+%20GetTimestamp()',100,'bob')
    Image_Downloader.download('http://xk.autoisp.shu.edu.cn:8080/Login/GetValidateCode?%20+%20GetTimestamp()',2,'bob')

