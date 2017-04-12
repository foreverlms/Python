#mar_28 Return function
# -*- coding: utf-8 -*-
def count() :
    fs=[]
    for i in range(1,4) :
        def f() :
            return  i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
a=f1()
print('%s %s %s'%(f1,f2,f3))
print(a)
#anoymous function
squares=[]
for x in range(5) :
    squares.append(lambda : x**2)
print(squares[2]()==squares[3]())
#This happens because x is not local to the lambdas, but
#  is defined in the outer scope, and it is accessed
# when the lambda is called — not when it is defined.
# At the end of the loop, the value of x is 4, so all
# the functions now return 4**2, i.e. 16. You can also
# verify this by changing the value of x and see how
# the results of the lambdas change:
#In order to avoid this, you need to save the values in
# variables local to the lambdas, so that they don’t rely
# on the value of the global x:
a=[]
for x in range(5) :
    a.append(lambda n=x: n**2)
print(a[2]()==a[3]())