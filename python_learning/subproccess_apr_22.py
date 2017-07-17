# import subprocess
#
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup',' www.python.org'])
# print('Exit code',r)

#nslookup 终端命令，需手动输入参数
#nslookup
#set q=mx
#python.org
#exit
# import subprocess
#
# print('$ nslookup')
# p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err=p.communicate(b'set q=mx\npython.org\exit\n')
# print(output.decode('gbk'))
# print('Exit code:',p.returncode)
#进程间通讯

from multiprocessing import Process,Queue
import os,time,random

def write(q) :
    print('Process to write :%s' %os.getpid())
    for value in ['A','B','C'] :
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q) :
    print('Process to read:%s',os.getpid())
    while True :
        value=q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__' :
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
