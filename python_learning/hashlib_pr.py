#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-13 19:14:11
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


import hashlib

# str_a="廖茂生"
# md5_simple=hash(str_a)
# print(md5_simple)

# md5=hashlib.sha256()
# print(type(md5))
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# md5.update('how to use md5 in python hashli?'.encode('utf-8'))
# print(md5.hexdigest())

# password_hash=hashlib.md5("Bobliao312".encode('utf-8'))
# db={
# 	'Bob' :password_hash
# }
# def login(user,password) :
# 	if user in db :
# 		return "Password "+str(db[user]==password)
# 	else:
# 		return "Your name is not correct"
# user_name=input('Please enter your name :')
# password=input('Please enter your psk :')
#
# print(login(user_name, password))

db={
	#store the username and password-hash
}
def register(username ,password) :
	if username in db :
		print("Username has existed.Change another username.")
	else :
		db[username]=get_md5(password)
		print('Registration Succeeded!')

def get_md5(password) :
	return hashlib.md5((password+'BL').encode('utf-8'))
def login(username, password) :
	if username not in db :
		print("Username doesn't exist.Please register first.")
	else :
		if db[username].hexdigest()==hashlib.md5((password+'BL').encode('utf-8')).hexdigest() :
			print(hashlib.md5().update((password+'BL').encode('utf-8')))
			print("Login succeed!")
		else :
			print('Password not correct.')
register('Bob','Bobliao312')
register('Bob','Bobliao312')
login('Bob','Bobliao3')