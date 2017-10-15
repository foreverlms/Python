#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-09-14 20:26:51
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\Pycharmprojects\Learning\code\craw_shu\grade_shu.py
# @Last Change : 2017-09-14 20:27:02

'''
Craw data of grade.
Dependencies:
	Selenium
	Pytesseract
	Tesseract OCR
'''

import pytesseract
import os
import re
import shutil
from PIL import Image

def traning_Tesseract(path) :
	'''
	批量转换jpg格式文件为tif格式到trainingdata文件夹
	:param path: 验证码JPG问件所在路径
	:return: None
	'''
	if os.path.isdir(path) :
		with os.scandir(path) as it :
			for entry in it :
				file, ext = os.path.splitext(entry.path)
				image=Image.open(entry.path)
				image.save(file+'.tiff','TIFF')
				# print(lambda x:x)
				shutil.move(file+'.tiff', '.\\traningdata\\')
class ParseGradeShu(object):
	"""This is a small crawler for SHU"""
	def __init__(self,sourceurl="http://cj.shu.edu.cn/"):
		super(ParseGradeShu, self).__init__()
		self.url=sourceurl
	
	def urlparse(self) :
		pass

	def getdata(self) :
		pass

class UnderGraduateParseGradeShu(ParseGradeShu):
	"""docstring for UnderGraduateParseGradeShu"""
	def __init__(self):
		super(UnderGraduateParseGradeShu, self).__init__()

if __name__ == '__main__':
	#第一次使用时运行
	traning_Tesseract(r'E:\Code\Python\Pycharmprojects\Learning\code\craw_shu\testdata')
	# with os.scandir(r'E:\Code\Python\Pycharmprojects\Learning\code\craw_shu\testdata') as it :
	# 	for entry in it :
	# 		text=pytesseract.image_to_string(Image.open(entry.path))
	# 		print(text)