#partial function
# def int2(x,base=2) : #base default value is 2,it can be changed
#     return int(x,base)#if we make the phrase liske this:return int(x,base=2),it will not be used to other radix
# print(int2('100',8))
# import functools
# #use functools.partial
# int3=functools.partial(int,base=8)
# a=int3('144')
# print(a)
# '''
# 模块（Java里面的.java文件？）
# '''
# 'a test module'
# _author_='Bob Liao'
import sys
# def test() :
#     args=sys.argv
#     if len(args)==1 :
#         print('hello world')
#     elif len(args)==2 :
#         print('hello %s'%args[1])
#     else :
#         print('too many arguments')
# if __name__=='__main__' :
#     test()
'''
有句话经典的概括了这段代码的意义：
“Make a script both importable and executable”
意思就是说让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行。
这句话，可能一开始听的还不是很懂。下面举例说明：
先写一个模块：
?
1
2
3
4
5
#module.py
def main():
  print "we are in %s"%__name__
if __name__ == '__main__':
  main()
这个函数定义了一个main函数，我们执行一下该py文件发现结果是打印出”we are in __main__“,说明我们的if语句中的内容被执行了，调用了main()：
但是如果我们从另我一个模块导入该模块，并调用一次main()函数会是怎样的结果呢？
?
1
2
3
#anothermodle.py
from module import main
main()
其执行的结果是：we are in module
但是没有显示”we are in __main__“,也就是说模块__name__ = '__main__' 下面的函数没有执行。
这样既可以让“模块”文件运行，也可以被其他模块引入，而且不会执行函数2次。这才是关键。
'''
from PIL import Image
for i in range(1,len(dir(Image))) :
    print(dir(Image)[i],end=' ')
    if(i%15==0) :
        print('\n')
print(help(Image))
im=Image.open('test.png')
print('\n')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thum.jpg','JPEG')
