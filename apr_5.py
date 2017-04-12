import logging
# logging.basicConfig(level=logging.INFO)
# def foo(s) :
#     n=int(s)
#     logging.info('n is %d' %n)
#     return 10/n
# print(foo('0'))
# print('End')
#############################
#with上下文管理器
# class Sample() :
#     def __enter__(self):
#         print('in __enter__()')
#         return 'foo'
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('in __exit()__')
# def getSample() :
#     return Sample()
# with getSample() as sample :
#     print("sample :",sample)
