#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-10-20 21:55:42
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\sublimeText\hipython_cousera\news_title\retrieve_data.py


import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
from datetime import date
import time
import numpy as np
from matplotlib import pylab as pb

def retrieve_quotes_historical(stock_code) :
	quotes=[]
	url='https://finance.yahoo.com/quote/{0}/history?p={1}'.format(stock_code,stock_code)
	req=requests.get(url,verify=True)
	if re.match(r'https://finance\.yahoo\.com/quote/(\w+)/history\?p=(\w+)',req.url):
		pass
	else :
		raise RequestException('Url is wrong!')
	if req.text :
		raw_data=re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"',req.text)
		if raw_data :
			quotes=json.loads(raw_data[0])[::-1]
	else :
		raise RequestException('URL Wrong!')
	return [item for item in quotes if not 'type' in item]

def get_historical_df(stock_code) :
	'''
		取得对应股票历史数据
	'''
	quotes=retrieve_quotes_historical(stock_code)
	quotesdf=pd.DataFrame(quotes)
	quotesdf=quotesdf.drop('adjclose',axis=1)
	date_list=[]
	month_list=[]
	for i in quotesdf['date'] :
		raw_date=date.strftime(date.fromtimestamp(i),"%Y-%m-%d")
		date_list.append(raw_date)
		raw_month=time.strptime(raw_date,"%Y-%m-%d").tm_mon
		month_list.append(raw_month)
	quotesdf.index=date_list
	quotesdf['month']=month_list
	quotesdf.drop('date',axis=1,inplace=True)
	return quotesdf

def get_code_list() :
	'''
		取得道指成分股代码基本信息
	'''
	req=requests.get('http://money.cnn.com/data/dow30/')
	raw_soup=BeautifulSoup(req.text,'html.parser')
	soupList=raw_soup.findAll('tr')
	del soupList[0:2]
	company_list=[soup.get_text().strip().replace('\xa0','\n').split('\n') for soup in soupList]
	return company_list

# print(get_code_list())