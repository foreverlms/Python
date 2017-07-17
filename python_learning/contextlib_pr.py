#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 11:52:34
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


#练习contextlib
#上下文管理器with自定义实现
# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')

#     def query(self):
#         print('Query info about %s...' % self.name)
# with Query('Bob') as q :
# 	q.query()
from contextlib import contextmanager

class Query(object):
	"""docstring for Query"""
	def __init__(self, name):
		super(Query, self).__init__()
		self.name = name
	def query(self) :
		print('Query info about %s...' %self.name)
#contextmanager装饰器用于上下文管理
@contextmanager
def create_query(name) :
	print('Begin')#此语句为__enter__()里面执行的语句
	q=Query(name)
	yield q#通过yield向with语句传递参数
	print('End')#yield之后的为__exit()__里面执行

with create_query('Bob') as q :
	q.query()
#例子2
@contextmanager
def tag(name) :
	print("<%s>" %name)
	yield#这里yield并没有传给with参数,因为with只是使用一个函数。
	print("</%s>" %name)

with tag("h1") :
	print('Hello')
	print('World')

#closing简单实现上下文，实际如下：
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page :
	for line in page :
		print(line)