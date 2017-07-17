import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue=queue.Queue()

result_queue=queue.Queue()

def return_task_queue() :
    global task_queue
    return task_queue
def return_result_queue() :
    global result_queue
    return result_queue
#从Basemanager继承而来的QueueManager
class Queuemanager(BaseManager) :
    pass
def test() :

    #将两个queue都注册到网络上，callable参数关联Queue对象
    Queuemanager.register('get_task_queue',callable=return_task_queue)
    Queuemanager.register('get_result_queue',callable=return_result_queue)
    #绑定端口5000，验证码为abc
    manager=Queuemanager(address=('127.0.0.1',5000),authkey=b'abc')
    manager.start()

    task=manager.get_task_queue()
    result=manager.get_result_queue()

    for i in range(10) :
        n=random.randint(0,1000)
        print('Put task %d in...' %n)
        task.put(n)

    print('Try get results...')
    for i in range(10) :
        n=random.randint(0,1000)
        r=result.get(timeout=10)
        print('Put task %d ...' %r)
    manager.shutdown()
    print('manager exit')
if __name__=='__main__' :
    freeze_support()
    test()