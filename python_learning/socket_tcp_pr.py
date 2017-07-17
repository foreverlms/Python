#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-19 22:38:31
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


import socket
import threading
import time
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.sina.com',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer=[]
# while True:
# 	d=s.recv(1024)
# 	if d :
# 		buffer.append(d)
# 	else :
# 		break
# data=b''.join(buffer)
# s.close()
# header,html=data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('from_socket_tcp_pr_sina.html','wb') as f :
# 	f.write(html)

socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.bind(('127.0.0.1',10000))
socket_server.listen(5)
print('Waiting for connection')
def tcplink(sock,addr) :
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit' :
			break
		#sock.send(bytes('Hello,%s!' %data,'utf-8'))
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s is closed' %addr)
while True:
	sock,addr=socket_server.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
	time.sleep(10)
