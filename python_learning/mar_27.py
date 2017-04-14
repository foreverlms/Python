# -*- coding:utf-8 -*-
#by Bob Liao
# x=['x','y',None,2]
# def empty(s) :
#     return s and s.strip()
# a='  123   '
# print(empty(a))
#filter usage
# def is_palidrome(n) :
#     if isinstance(n,int) :
#         nstr=str(n)
#         nreverse=int(nstr[::-1])
#         if n==nreverse :
#             return True
# output=filter(is_palidrome,range(1,1000))
# print(list(output))
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',68)]
def by_name(t) :
    if isinstance(t,tuple) :
        return t[0]
L2=sorted(L,key=by_name)
print(L2)
