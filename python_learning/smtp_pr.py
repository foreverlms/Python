#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 19:57:10
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


from email.mime.text import MIMEText
import smtplib

msg=MIMEText('I Love you.','plain','utf-8')
# from_addr=input('From: ')
# pass_word=input('Password: ')
# to_addr=input('To: ')
# smtp_server=input('SMTP Server: ')
from_addr='codechaser@163.com'
#授权码，非用户登录密码
pass_word='icui4cu'
to_addr='1430752920@qq.com'
smtp_server='smtp.163.com'

try:
	server=smtplib.SMTP_SSL(smtp_server,465)
	server.set_debuglevel(1)
	server.login(from_addr, pass_word)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()		
except smtplib.SMTPAuthenticationError:
	print("Please ensure that your email-account \
		exists and password is correct")