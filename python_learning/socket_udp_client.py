#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 13:10:54
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


import socket

socket_udp_client=socket.socket(type=socket.SOCK_DGRAM)
for data in [b'Bob',b'Liao'] :
	socket_udp_client.sendto(data, ('127.0.0.1',9999))
	print(socket_udp_client.recv(1024).decode('utf-8'))
socket_udp_client.close()