#! /usr/bin/env/python

import struct
import os
# print(struct.pack('>I',10240099))
#
# print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
#
# f=open('test.bmp','rb')
# s=f.read(30)
# f.close()
# print(struct.unpack('<ccIIIIIIHH',s))
#廖雪峰测试题
#编写一个bminfo.py。可以检查任意文件是否为位图文件，若果是，打印出图片大小和颜色数
def bmp_tell(path) :
    if os.path.isfile(path) :
        f=open(path,'rb')
        s=f.read(30)
        f.close()
        judge_condition=s[0:1].decode()+s[1:2].decode()
        print(judge_condition)
        if judge_condition =='BM' or judge_condition == 'BA':
            print('This file is a BMP File')
            bmp_info=struct.unpack('<ccIIIIIIHH',s)
            print('This bmp file is %sx%s and has %s kinds of color' %(bmp_info[6],bmp_info[7],bmp_info[-1]))
        else:
            print('This file isn\'t a BMP File')
    else:
        print('This path is not a file')
bmp_tell('test.bmp')
a={1:3,2:2,3:3}
b=sorted(a.keys())
print(','.join([str(i) for i in b ]))