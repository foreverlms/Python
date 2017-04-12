#iterator
#汉诺塔移动圆盘问题，递归真的很精妙
'''
def move(n,a,b,c) :
    if n==1 :
        print(a+'-->'+c)
    #如果只有a柱上只有一个圆盘，直接由a-->c
    else :
            move(n-1,a,c,b)
            #将n-1个圆盘移到b
            move(1,a,b,c)
            #将第n个盘子移到c上
            move(n-1,b,a,c)
            #重复n-1个盘子从b到c上，a成为中间柱
move(3,'A','B','C')
'''
#循环？
'''
L=[]
n=1
while n<100 :
    L.append(n)
    n=n+2
print(L)
'''
# Slice practice
ListA=['Bob','Wang','Liao','Daddy']
print(ListA)
print(ListA[0:2])
#截取0,1index的list元素，不包括end_index元素
print(ListA[:2])
#缺省start_index，默认从第一个元素开始切片
print(ListA[-2:-1])
#从-2开始到-1index，不包括end_index元素（-1）
print(ListA[-2:])
#缺省end_index，默认切片至list最后一位
print(ListA[::-1])
print(ListA[::-3])
#缺省start_index和end_index，
print(ListA)
ListA.reverse()
print(ListA)