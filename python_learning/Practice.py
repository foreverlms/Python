# -*- coding: utf-8 -*-


#输出字符串的奇数位
# def odd() :
#     n=1
#     while True :
#         yield n
#         n+=2
#     return 'done'
# a='xyzabcd'
# b=odd()
# for i in b :
#     if i>=len(a)+1 : break
#     print(a[i-1],end='')

#输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
# import math
# def is_prime(num) :
#     if num<2 :
#         return False
#     else:
#         for i in range(2,int(math.sqrt(num))+1) :
#             if num%i==0 :
#                 return False
#         return True
#
# primes=[]
# for i in range(101) :
#      if is_prime(i):
#          primes.append(i)
# # for i in range(len(primes)-1) :
# #     print(primes[i],end=' ')
# # print(primes[-1])
# print(' '.join(map(str,primes)))

#输出矩形面积周长
# a=3;b=8
# def sq_ci(a,b) :
#     return str(a*b),str(2*(a+b))
# print(' '.join(sq_ci(a,b)))
# 给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。
#
# 例如： L=[0,1,2,3,4]
#
# 则输出：2
# L=[0,1,2,3,4]
# a=sorted(L)
# if len(L)%2==0 :
#     median_fl=(a[len(L)//2]+a[len(L)//2-1])/2.0
#     median=str(median_fl)
#     dot_pos=median.index('.')
#     print(median[:(dot_pos+2)])
# else :
#     median_fl=a[len(L)//2]
#     median = str(median_fl)
#     try :
#         dot_pos = median.index('.')
#         print(median[:(dot_pos +2)])
#     except ValueError :
#         print(median)

##求最大公约数
# a=3;b=5
# c=min(a,b)
# d=max(a,b)
# i=c
# while i>0 :
#     if c%i==0 and d%i==0 :
#         print(i)
#         break
#     i-=1

#给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
# L=[2,8,3,50]
# def count_zero(num) :
#     num_2=0
#     num_5=0
#     num_cp=num
#     while num%2==0 and num!=0 :
#         num_2+=1
#         num/=2
#     while num_cp%5==0 and num!=0 :
#         num_5+=1
#         num_cp/=5
#     return num_2,num_5
# num_2=0
# num_5=0
# for i in L :
#     num_2+=count_zero(i)[0]
#     num_5+=count_zero(i)[1]
# print(min(num_5,num_2))
#光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。小Py光棍几十载，光棍自有光棍的快乐。让我们勇敢地面对光棍的身份吧，现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出。
# from functools import reduce
# print('\033[1;31;40m')
# print('*'*50)
# print("URI:\t","https://www.baidu.comn\n")
# def multi(a,b) :
#     return a*b
# L=[1,2,3,4,5]
# result=str(reduce(multi,L))
# for i in reversed(result) :
#     num=int(i)
#     if num!=0 :
#         if num%2==0 :
#             print('0')
#             break
#         print('1')
#         break
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('start_tag <%s>' % tag)

    def handle_endtag(self, tag):
        print('end_tag </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('start_end_tag <%s/>' % tag)

    def handle_data(self, data):
        print(data.encode('utf-8'))

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('100&%s;' % name)

    def handle_charref(self, name):
        print('100&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')