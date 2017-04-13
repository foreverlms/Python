#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tickets viewer on cmd

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help 	show the helping menu
	-g 			gaotie
	-d 			dongche
	-t 			tekuai
	-k 			kuaisu
	-z 			zhida

Example:
	tickets beijing shanghai 2016-10-10
	tickets -dg chengdu nanjing 2016-10-10
"""
from docopt import docopt
from stations import stations
import json
import requests

def cli():
	"""command-line interface"""
	arguments=docopt(__doc__)
	from_station=stations.get(arguments['<from>'])
	to_station=stations.get(arguments['<to>'])
	train_date=arguments['<date>']
	url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
		train_date,from_station,to_station
		)
	r=requests.get(url,verify=False)
	#print(r.json())
	with open('./a.json','w') as f:
		a=json.dumps(r.json())
		f.write(a)

if __name__ == '__main__':
	cli()