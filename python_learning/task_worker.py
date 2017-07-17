#!/usr/bin/python3.4

import random,time,queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager) :
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='127.0.0.1'

print('Connect to server %s ...' % server_addr)

m=QueueManager(address=(server_addr,5000),authkey=b'abc')

m.connect()

task=m.get_task_queue()

result=m.get_result_queue()

for i in range(10) :
	try:
		n=task.get(timeout=1)
		print('run task %d * %d' %(n.n))
		r='%d * %d=%d' %(n,n,n*n)
		time.sleep()
		result.put(r)
	except Queue.Empty :
		print('task queue is empty.')
print('Work exit.')

# manager=QueueManager(address=('',5000),authkey=b'abc')

# manager.start()

# task=manager.get_task_queue()
# result=manager.get_result_queue()

# for i in range(10) :
# 	n=random.randint(0,1000)
# 	print('Put task %d...' %n)
# 	task.Put(n)

# print('Try get results...')

# for i in range(0,1000) :
# 	r=result.get(timeout=10)
# 	print('Result is %s' % r)

# manager.shutdown()
# print('Master exit')