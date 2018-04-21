#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
# @Date    : 2018-04-20 00:31:57
# @Author  : Bob Liao (codechaser@163.com)
# @Link    : https://github.com/coderchaser

import logging
import os
from functools import wraps

#set the handler string format
FORMAT = '%(asctime)-15s %(filename)s %(message)s %(imageurl)s %(imagename)s'
logging.basicConfig(format=FORMAT,level=logging.INFO,filename="biaoqingDownloader.log",datefmt="[%Y-%m-%d %H:%M:%S]")
my_log_extra={"imageurl" :"","imagename":""}

#downloader logger
def downloader_logger(func) :
	@wraps(func)
	def wrapper(*args, **kwargs) :
		func(*args,**kwargs)
		try:
			image_name=args[0]
			image_url=args[1]
		except KeyError as e:
			raise e
		my_log_extra["imagename"]=image_name
		my_log_extra["imageurl"]=image_url
		logging.info("biaoqingbaoDownloader downloaded image:",extra=my_log_extra)
	return wrapper

if __name__ == '__main__':
	## test this logger
	@downloader_logger
	def foo(filename,imageurl) :
		print('logging test')

	foo('test.png','www.baidu.com')
	#if no error appears, clear the log file
	with open('./biaoqingDownloader.log','w') as f :
		f.truncate()
