#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tickets viewer on cmd

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help 		显示帮助栏
	-g 			高铁
	-d 			动车
	-t 			特快
	-k 			快速
	-z 			直达

Example:
	tickets 北京 上海 2016-10-10
	tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt
from prettytable import PrettyTable
from stations import stations
from colorama import init,Fore
#import json
import requests

init()

class TrainsCollections(object):
	header='车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

	def __init__(self,avaliable_trains,options) :
		self.avaliable_trains=avaliable_trains
		self.options=options
	def _get_duration_(self,raw_train) :
		duration=raw_train.get('lishi').replace(':','小时')+'分'
		if duration.startswith('00') :
			return duration[4:]
		if duration.startswith('0') :
			return duration[1:]
		return duration
	@property
	def trains(self) :
		for init_raw_train in self.avaliable_trains:
			raw_train=init_raw_train['queryLeftNewDTO']
			train_no=raw_train['station_train_code']
			initial=train_no[0].lower()
			if not self.options or initial in self.options:
				train =[
					train_no,
					'\n'.join([Fore.GREEN+raw_train['from_station_name']+Fore.RESET,
						Fore.RED+raw_train['to_station_name']+Fore.RESET]),
					'\n'.join([Fore.GREEN+raw_train['start_time']+Fore.RESET,
						Fore.RED+raw_train['arrive_time']+Fore.RESET]),
					self._get_duration_(raw_train),
					raw_train['zy_num'],
					raw_train['ze_num'],
					raw_train['rw_num'],
					raw_train['yw_num'],
					raw_train['yz_num'],
					raw_train['wz_num']
				]
				yield train
	def prettyprint(self) :
		pt=PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains :
			pt.add_row(train)
		print(pt)
		
def cli():
	"""command-line interface"""
	arguments=docopt(__doc__)
	from_station=stations.get(arguments['<from>'])
	to_station=stations.get(arguments['<to>'])
	train_date=arguments['<date>']
	url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
		train_date,from_station,to_station
		)
	options=''.join([key for key,value in arguments.items() if value is True])
	r=requests.get(url,verify=False)
	avaliable_trains=r.json()['data']
	TrainsCollections(avaliable_trains,options).prettyprint()
	
	

if __name__ == '__main__':
	cli()
