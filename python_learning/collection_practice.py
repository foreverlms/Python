#!/usr/bin/env python3

#test built_in modules collections
#collections包含了很多有用的集合类

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


#用tuple表示一个点的坐标，不用建一个类，利用nametuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
#创建一个circle(tuple)类
Circle=namedtuple('Circle',['x','y','r'])
circle_a=Circle(1.0,2.0,5.0)
print(circle_a)
#deque（双端队列）
q=deque(['a','b','c'])
q.append('x')
q.append(20)
q.appendleft('z')
print(q)
q.pop()
print(q)
#defaultdict当索引的key不存在时会返回默认值，其余与普通dict一样
dd=defaultdict(lambda :'No such key')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])
#ordereddic key有顺序的dict
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)

#OrderDict 可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的key

class LastUpdateOrderDict(OrderedDict) :
    def __init__(self,capacity):
        super(LastUpdateOrderDict,self).__init__()
        self._capacity=capacity
    def __setitem__(self, key,value):
        containsKey=1 if key in self else 0
        if len(self)-containsKey>=self._capacity:
            last=self.popitem(last=False)
            print('remove',last)
        if containsKey:
            del self[key]
            print('set',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)
a=LastUpdateOrderDict(2)
a.__setitem__('a',1)
a.__setitem__('b',2)
print(a)
a.__setitem__('c',3)
print(a)
#counter测试
c=Counter()
for ch in "bobliao" :
    c[ch]=c[ch]+1
print(c)
