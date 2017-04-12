# -*- coding: utf-8 -*-
#今天了解了list、tuple、dictionary、set这些类型
import  math
'''
height=float(input("Please input your height"))
weight=float(input("Please input your weight"))

#get the BMI
BMI=float(weight*weight/height)
if BMI<=18.5 :
    print("too light")
elif BMI<=25 and BMI>18.5 :
    print("normal")
elif BMI<=28 and BMI>25 :
    print("overweight")
elif BMI<=32 and BMI>28 :
    print("fat")
else:
    print("too fat")

a=range(10) #rang返回的不是一个list？
print(list(range(5)))
print(a.index(9))
names=["Michael","Bob",'Helen']
for name in names:
    print("Hello,",name+'!')
'''''
#dictionary类型应用
'''d={"Michael": 17,"Bob": 18,"Helen": 17}
print(d["Michael"])
print("Bob" in d)
print(d.get("Levin","no this guy"))
print(d.values())'''
#调用、定义函数

'''def swap(a,b):
    temp=a
    a=b
    b=temp
x=10
y=12
a,b=10,12
a,b=b,a
swap(x,y)
print(a,b)
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and not isinstance(b,(int,float)) and not isinstance(c,(int,float)) :
        raise TypeError("Wrong type for factors")
    if (b**2-4*a*c)<0:
        return "No solutions"
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    print(x1)
    x2=-(-b+math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2
a=quadratic(1,3,2)
print(quadratic(1,3,2))
print(a[1])
print(a)'''

