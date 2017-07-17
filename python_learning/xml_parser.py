#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 21:20:01
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4


from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
# 	"""docstring for DefaultSaxHandler"""
# 	def start_element(self,name,attrs) :
# 		print('sax:start_element: %s,attrs : %s' %(name,str(attrs)))

# 	def end_element(self,name) :
# 		print('sax:end_element : %s' % name)

# 	def char_data(self,text) :
# 		print('sax:char_data :%s' % text)

# xml=r'''<?xml version="1.0"?>
# <ol>
#      <li><a href="/python">python</a></li>
#      <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# handler=DefaultSaxHandler()
# parser=ParserCreate()
# parser.StartElementHandler=handler.start_element
# parser.EndElementHandler=handler.end_element
# parser.CharacterDataHandler=handler.char_data
# parser.Parse(xml)

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
weather_dic=dict()
day=0
class WeatherSaxHandler(object):
	"""docstring for WeatherSaxHandler"""
	# def __init__(self) :
	# 	self.weather=dict()
	def start_element(self,name,attrs) :
		global weather_dic
		global day
		if name=="yweather:location" :
			weather_dic['city']=attrs['city']
			weather_dic['country']=attrs['country']
		if name=="yweather:forecast" :
			day+=1
			if day==1 :
			#<yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
				today={}
				today['text']=attrs['text']
				today['low']=int(attrs['low'])
				today['high']=int(attrs['high'])
				weather_dic['today']=today
			if day==2 :
				tomo={}
				tomo['text']=attrs['text']
				tomo['low']=attrs['low']
				tomo['high']=attrs['high']
				weather_dic['tomorrow']=tomo
	def cha_data(self,text) :
		pass
	def end_element(self,name) :
		pass
weather_handler=WeatherSaxHandler()
weather_parser=ParserCreate()
weather_parser.StartElementHandler=weather_handler.start_element
weather_parser.Parse(data)
print(weather_dic)