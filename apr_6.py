#reading files
# with open(r'C:\Users\Bobliao\PycharmProjects\Learning\test.txt','r',encoding='utf-8') as f :
#     print(f.read())
# with open(r'C:\Users\Bobliao\PycharmProjects\Learning\test.txt','a',encoding='utf-8') as f:
#     s=input('please input a string :')
#     f.write(s+'\n')
from io import StringIO,BytesIO
astring=StringIO('I love you\nI love the world\n')
abytes=BytesIO('廖茂生'.encode())
while True :
    s=astring.readline()
    if isinstance(s,str) and  s=='' :
        break
    print(s.strip())
print(abytes.getvalue())
a=['a','b']
b=['a','b']
print(a is b)#False
