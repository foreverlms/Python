#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 09:08:19
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


import sqlite3

connect_db=sqlite3.connect('test.db')

cursor=connect_db.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.execute('select * from user where name =?',('Michael',))
result=cursor.fetchall()
print(result)
cursor.close()
cursor1=connect_db.cursor()
cursor1.execute('insert into user (id, name) values (\'2\', \'Bob\')')
cursor1.execute('select * from user where name =?',('Bob',))
result1=cursor1.fetchall()
print(result1)
cursor1.close()