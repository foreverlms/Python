#april 2nd python learning
from types import MethodType
# class Student(object) :
#     pass
# s=Student()
# s.name='Bob'
# def set_age(self,age) :
#     self.age=age
# s.set_age=MethodType(set_age,s)
# s.set_age(25)
# print(s.name,s.age)#just one instance(s) has a method set_age
# print(dir(s))
# def set_score(self,score) :
#     self.score=score
# Student.set_score=set_score
# s.set_score(100)
# print(s.score)
#use __slots__to restrict attribute
#########################################
# class Student1(object) :
#     a=10
#     __slots__ = ('__name','__score','__age')#restrict the number of Student1
#     def __init__(self,name,score,age) :
#         self.__name=name
#         self.__score=score
#         self.__age=age
#     def getAttributes(self):
#         a=(self.__name,self.__score,self.__age)
#         return a
# a=Student1('Bob',90,22)
# print(a.getAttributes())#we can not add some attributes like 'concentration'into the Class Student1
# class Student2(Student1) :
#     pass
# b=Student2('Wang',90,23)
# print(b.getAttributes())
# b.concentration='Mech'
# print(b.concentration)
# print(dir(b))
# def setAccademy(self,accademy) :
#     self.accademy=accademy
# Student2.setAccademy=MethodType(setAccademy,Student2)
# print(dir(Student2))
# Student2.b=10
# print(dir(Student2))
class Screen(object):
    def __init__(self):
        self._width=10
        self._length=10
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer')
        self._width=value
    @property   ###############property
    def length(self):
        return self._length#此处Student类中已有length属性，不能再用一个self.length属性，所以前面加一个_下划线
    @length.setter
    def length(self,length):#参考width装饰器，此处位置参数length最好不要和前面的length.setter同名
        if not isinstance(length,int) :
            raise ValueError('length must be an integer')
        self._length=length
    @property
    def resolution(self):
        return self._width*self._length     #read only
s=Screen()
s.width=1024
s.length=768
print(dir(Screen))
print(dir(s))
print(s._length)
print(s.resolution)