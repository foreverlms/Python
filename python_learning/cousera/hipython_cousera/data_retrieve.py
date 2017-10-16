#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-10-12 22:45:19
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\sublimeText\hipython_cousera\data_retrieve.py


import requests
from requests import RequestException
import re
import json
import pandas as pd
from datetime import date
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab as pb
def retrieve_quotes_historical(stock_code) :
	quotes=[]
	url='https://finance.yahoo.com/quote/{0}/history?p={1}'.format(stock_code,stock_code)
	req=requests.get(url,verify=True)
	if req.text :
		raw_data=re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"',req.text)
		if raw_data :
			quotes=json.loads(raw_data[0])[::-1]
	else :
		raise RequestException('URL Wrong!')
	return [item for item in quotes if not 'type' in item]

def get_df(stock_code) :
	quotes=retrieve_quotes_historical(stock_code)
	quotesdf=pd.DataFrame(quotes)
	quotesdf=quotesdf.drop('adjclose',axis=1)
	date_list=[]
	month_list=[]
	for i in quotesdf['date'] :
		raw_date=date.strftime(date.fromtimestamp(i),"%Y%m%d")
		date_list.append(raw_date)
		raw_month=time.strptime(raw_date,"%Y%m%d").tm_mon
		month_list.append(raw_month)
	quotesdf.index=date_list
	quotesdf['month']=month_list
	quotesdf.drop('date',axis=1,inplace=True)
	return quotesdf
intel_df=get_df('INTC')
# intel_df.to_excel('intel.xls')
ibm_df=get_df('IBM')
# ibm_df.to_excel('ibm.xls')
volumes_intel=intel_df.groupby('month').volume.sum()
volumes_ibm=ibm_df.groupby('month').volume.sum()
volumes_df=pd.DataFrame([volumes_intel,volumes_ibm]).T
volumes_df.columns=['Intel','Ibm']
# volumes_df.plot(kind='bar')
volumes_intel.plot(kind='pie',subplots=True,autopct='%.2f',legend=True,label='Month')
plt.legend(loc='lower right',bbox_to_anchor=(1.13,0.2))
plt.show()
