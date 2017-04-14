# _*_ coding:utf-8 _*_
#iteration
# dic1 the second 'Bob''s value was replaced by 20
# dic1={'Bob':17,'Liao':'name','Bob':20}
# for name in dic1 :
#     print(name)
# for key,values in dic1.items() :
#     print(key)
#     print(values)
# for i in 'ABC V' :
#     print(i)
#use Class Iterable to judge whether an object is iterable
# from collections import Iterable
# print(isinstance('abc',Iterable))
# l=[m+'='+n.__str__() for m,n in {'a':1,'b':2}.items()]
# print(l)
# #fast ways to generate List class
# L1=['Hello','world',18,'Apple','China']
# L2=[s.capitalize() for s in L1 if isinstance(s,str)]
# print(L2)
#generators
# def triangles() :
#     L=[1]
#     generatorWorks=True
#     while generatorWorks :
#         yield L
#         #L=[[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]]
#         L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0) #这里好巧妙，来自http://www.liaoxuefeng.com/wiki/0014316089557264a6b348
#         # 958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000#0
#         #苏格兰折耳喵的作业
#         L = [L[i - 1] + L[i] for i in range(len(L))]
# n=0
# for t in triangles() :
#     print(t)
#     n=n+1
#     if n>=10 :
#         break
#map
# def f(x) :
#     return x*x
# L=[1,2,3,4,5]
# r=map(f,L)
# print(list(r))
#refuce
from functools import reduce
# def summyself(x,y) :
#     return x+y
# print(reduce(summyself,[0,1,2,3,4,5]))
def Captalize(n) :
    if isinstance(n,str) :
        return n.capitalize()
    else :
        return False
L=['adam','LISA','barT']
print(list(map(Captalize,L)))
def prod(n) :
    def multi(x,y) :
        return x*y
    if isinstance(n,list) :
        return reduce(multi,n)
print(prod([1,2,3,4]))
def str2float(str1) :
    if isinstance(str1,str) :
        a=str1.index('.')
        sub1=str1[0:a]
        sub2=str1[a+1:]
        def chrstr(s) :
            return {'0': 0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
        def fn1(x,y) :
            return x*10+y
        int1=reduce(fn1,map(chrstr,sub1))
        int2=reduce(fn1,map(chrstr,sub2))
        return float(int1)+float(int2/(10**len(sub2)))
    else:
        return False
print(str2float('123.456'))