#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 19:57:20
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


import poplib
from email.parser import Parser
from email.header import decode_header
# email = input('Email: ')
# password = input('Password: ')
# pop3_server = input('POP3 server: ')
email_addr='codechaser@163.com'
pass_word='icui4cu'
pop3_server='pop.163.com'

server=poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email_addr)
server.pass_(pass_word)

print('Messages: %s.Size: %s' % server.stat())

resp,mails,octets=server.list()
print(mails)

index=len(mails)
resp,lines,octets = server.retr(index)

msg_content=b'\r\n'.join(lines).decode('utf-8')
msg=Parser().parsestr(msg_content)