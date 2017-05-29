#!/usr/bin/env/python3
#coding :utf-8
import uuid

# use UUID to generate unique coupons
def geberate_coupons(num) :
	#generate coupons
	codes=[]
	for i in range(num) :
		code=str(uuid.uuid4()).replace('-', '').upper()
		while code in codes :
			code=str(uuid.uuid4()).replace('-', '').upper()
		codes.append(code)
	for i in codes :
		print(i)
	return codes
def write_in(coupons) :
	#record the coupons into .txt file
	with open('coupons.txt','w',encoding='UTF-8') as f :
		for i in coupons:
			f.write(i+'\n')
	
if __name__ == '__main__':
	write_in(geberate_coupons(10))