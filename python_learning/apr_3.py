# -*- coding:utf-8 -*-
############################
# class Student() :
#     def __init__(self):
#         self.name=['a','b','c']
#     def __len__(self):
#         return len(self.name)
# s=Student()
# print(len(s))
# print(dir(s))
#############################
# class Student() :
#     def __init__(self,=''):
#         self.__name='Bob'
#         self.__=
#     def __str__(self):
#         print('This student\' name is '+self.__name)
#         return self.__
#     def __getattr__(self, item):
#         return Student('%s/%s' %(self.__path,item))
#     __repr__=__str__
# print(Student().users.timelist.list)#使用__getattr__来实现动态添加属性
############################################
#Enum使用
# from enum import Enum
# Month=Enum('Month',('JAN','FEB','MAR','APR','MAY','JUL','JULY','AUG','SEP','OCT','NOV','DEC'))
# for name ,member in Month.__members__.items() :
#     print(name,'=>',member,',',member.value)
# print(Month.__members__.items)
# print(Month._member_map_)
##########################################
# def fn(self,name='world') :
#     print('Hello,%s' %name)
# s=type('hello',(object),dict(hello=fn))#利用type创建类
########################################
#错误异常
# def divide() :
#     divided=int(input('Please input the divided number'))
#     divide=int(input('Please input the divide number'))
#     try :
#         print('try')
#         result=divided//divide
#         print(result)
#     except ZeroDivisionError as e:
#         print('except',e)
#     finally:
#         print('finally')
#     print('End call')
# divide()
################################################
# class BobError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise BobError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except BobError as e:
#         print('TestError!')
#         raise
# bar()
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
        print('End')
bar()
'''
bar()->foo('0')->抛出ValueError('invalid value: %s' % s)错误，不能处理，交由上层调用者bar()处理->bar()exceptValueError错误
，打印ValueError，继续raise抛出ValueError('invalid value: %s' % s)错误，交由上一级处理，没有处理，最终交由解释器处理并中断
程序，导致print('End')没有执行
'''