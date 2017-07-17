#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 18:03:31
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


import socket
import threading
socket_udp_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_udp_server.bind(('127.0.0.1',9999))
print('Binded to %s:%s.' %socket_udp_server.getsockname())
while True:
	data,addr=socket_udp_server.recvfrom(1024)
	print('Received from %s:%s.' %addr)
	socket_udp_server.sendto(b'Hello,%s' %data,addr)
