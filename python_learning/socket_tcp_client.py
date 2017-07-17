#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-21 19:34:58
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4

import socket
socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_client.connect(('127.0.0.1',10000))
print(socket_client.recv(1024).decode('utf-8'))
for data in [b'Bob',b'Liao'] :
	socket_client.send(data)
	print(socket_client.recv(1024).decode('utf-8'))
socket_client.send(b'exit')
socket_client.close()