#decorator
import functools
def log(received='call') :
    def decorator(func) :
        @functools.wraps(func)
        def wrapper(*args,**kw) :
            print("begin %s %s()" %(received,func.__name__))
            result=func(*args,**kw)
            print('%s %s()'%(received,func.__name__))
            print("end %s %s()" % (received, func.__name__))
            return result
        return wrapper
    return decorator
@log
def f1() :
    pass
@log('execute')
def f2() :
    pass
def log1(func) :
    @functools.wraps(func)
    def wrapper(*args,**kw) :
        print('call', func.__name__)
        return func(*args,**kw)
    return wrapper
@log1
def f3() :
    pass
f1()
f2()
f3()
###################################
# def log(t):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print(t+'begin call')
#             result=func(*args,**kw)
#             print(t+'end call')
#             return result
#         return wrapper
#     if isinstance(t,str):
#         return decorator
#     else:
#         f=t
#         t=''
#         return decorator(f)
#
# @log
# def a():
#     print('现在时间')
# a()
# @log('hello')
# def a():
#     print('现在时间')
# a()
# def f() :
#     print('hellp')
