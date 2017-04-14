# -*- coding: utf-8 -*-
'''
#*L可变参数
def sum(*L) :
    sum=0
    for i in L:
        sum+=i
    return sum
print(sum(1,2,3,4,5))
num=[1,2,3,4,5,6]
print(sum(*num))
#默认参数
def haha(name,year,city='Shanghai') :
    print("your name is",name,"you are",year,"years old","you live in",city)
haha('Bob',22)
'''
#命名关键字参数
def sum(*L) :
    sum=0
    for i in L:
        sum+=i
    return sum
def person(name,college,gender='M',*grades,**kw) :
    print("Your name is",name,"your college is",college,"your gender is",gender,'\n')
    print("Your summary grades is", sum(*grades))
    print(kw.keys())
    print(kw.values())
person('Bob','SHU',100,50,100,city='Shanghai',province='Henan')
def f1(a,b,c=0, *args, **kw):
    print('a =',a,'b =',b,'c =',c,'args =',args,'kw =',kw)
args=(1, 2, 3, 4)
kw={'d': 99, 'x': '#'}
f1(*args, **kw)