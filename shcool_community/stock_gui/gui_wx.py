#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-10-20 21:56:09
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\sublimeText\hipython_cousera\news_title\gui_wx.py


from matplotlib import pyplot as plt
import pandas as pd
import wx
import threading
import retrieve_data as rd
import io
import _thread as thread
import time

ID_LIST_CTRL=1234

class MyFrame(wx.Frame) :
	'''
		Frame用于道指成分股图表生成
	'''
	def __init__(self,title) :
		super(MyFrame,self).__init__(None,title=title,size=(600,600))
		self.date=time.strftime("%a,%d,%b,%Y",time.gmtime())
		self.CreateStatusBar()
		# self.Center()
		self.InitUI()

	def InitUI(self) :
		self.OptionList={
		'open':True,
		'close':True,
		'high' :False,
		'low':False,
		'volume':False
		}
		self.box_dict={
			"开盘价":True,
			"收盘价":True,
			"最高价":False,
			"最低价":False,
			"交易总量":False
		}#复选框选项
		image=open('stocks.png','rb')#icon源文件
		image=wx.Bitmap(wx.Image(image))
		icon_=wx.Icon()
		icon_.CopyFromBitmap(wx.Bitmap(image))
		self.SetIcon(icon_)

		#菜单选项
		self._menu=wx.MenuBar()
		filemenu=wx.Menu()
		save_menu=wx.MenuItem(filemenu,wx.ID_SAVE,text='保存')
		#TODO:add handlers
		refresh_menu=wx.MenuItem(filemenu,wx.ID_REFRESH,'刷新')
		self.Bind(wx.EVT_MENU,self.OnRefresh,refresh_menu)
		filemenu.Append(save_menu)
		filemenu.Append(refresh_menu)
		filemenu.Append(wx.ID_EXIT,'退出',"退出应用")
		self.Bind(wx.EVT_MENU,self.OnQuit,id=wx.ID_EXIT)
		self._menu.Append(filemenu,"File")
		self.SetMenuBar(self._menu)

		#各个组件
		self.panel=wx.Panel(self)
		sizer=wx.BoxSizer(wx.VERTICAL)#总的布局管理
		hboxSizer=wx.BoxSizer(wx.HORIZONTAL)#staticText和textCtrl水平管理
		code_label=wx.StaticText(self.panel,label='股票代码： ')
		hboxSizer.Add(code_label,0,wx.ALIGN_CENTER)
		code_text=wx.TextCtrl(self.panel,value='BA',style=wx.TE_PROCESS_ENTER)
		date_text=wx.StaticText(self.panel,wx.ALIGN_CENTER,label=self.date)
		self.Bind(wx.EVT_TEXT_ENTER,self.OnCodeText,code_text)
		#TODO: add code_text handler
		hboxSizer.Add(code_text)
		hboxSizer.AddSpacer(5)
		hboxSizer.Add(date_text,0,wx.ALIGN_CENTER)

		checkboxSizer=wx.BoxSizer(wx.HORIZONTAL)#复选框水平布局管理
		for key,value in self.box_dict.items() :
			checkbox=wx.CheckBox(self.panel,label=key)
			checkbox.SetValue(value)
			checkboxSizer.Add(checkbox)
			self.Bind(wx.EVT_CHECKBOX,self.OnChecked)

		self.list_ctrl=wx.ListCtrl(self.panel,id=ID_LIST_CTRL,style=wx.LC_REPORT)
		# self.list_ctrl.Center()
		self.createHeader()
		self.list_index=0
		pos=self.list_ctrl.InsertItem(0,'------')
		self.list_ctrl.SetItem(pos,3,"loading...")
		self.list_ctrl.SetItem(pos,1,"------")
		self.list_ctrl.SetItem(pos,2,"------")
		self.list_ctrl.SetItem(pos,4,"------")
		self.list_ctrl.SetItem(pos,5,"------")
		self.list_ctrl.SetItem(pos,6,"------")
		self.list_ctrl.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnListItemRightClick)#右键条目
		self.list_ctrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.OnDoubleClick)#双击出图
		
		buttonSizer=wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer.Add((10,10))
		quitButton=wx.Button(self.panel,label='退出')
		refreshButton=wx.Button(self.panel,label='刷新')
		self.Bind(wx.EVT_BUTTON,self.OnQuit,quitButton)
		self.Bind(wx.EVT_BUTTON,self.OnRefresh,refreshButton)
		buttonSizer.Add(quitButton,wx.ALIGN_CENTER,border=5)
		buttonSizer.Add(refreshButton,wx.ALIGN_CENTER,border=5)


		sizer.Add(hboxSizer,0,wx.ALL,5)
		sizer.Add(checkboxSizer,0,wx.ALL,5)
		sizer.Add(self.list_ctrl,-1,wx.ALL | wx.EXPAND,5)
		sizer.Add(buttonSizer,0,wx.ALIGN_CENTER | wx.EXPAND,5)
		self.panel.SetSizerAndFit(sizer,wx.EXPAND |wx.ALL)

		self.OnRefresh(None)#初始化ListCtrl

	def OnCodeText(self,event) :
		'''
			文本框事件处理
		'''
		code=event.GetEventObject().GetValue()
		self.PlotData(code)

	def OnDoubleClick(self,event) :
		text=event.GetText()
		self.PlotData(text)

	def PlotData(self,code) :
		'''
			出图，因为volume值太大，如果勾选，和别的数据分开来
		'''
		df=rd.get_historical_df(code)
		drop_list=['month']
		for key,value in self.OptionList.items() :
			if not value :
				drop_list.append(key)
		if 'volume' not in drop_list :
			figure1=plt.figure('Volume')
			df.volume.plot()
			plt.title('Volume')
			plt.xlabel('Date')
			plt.ylabel('Value')
			figure1.show()
			df.drop('volume',axis=1,inplace=True)#drop函数如果inplace不设为True就不会改变df本身
		df=df.drop(drop_list,axis=1)
		df.plot()
		plt.title(code)
		plt.xlabel('Date')
		plt.ylabel('Value')
		# figure2.show()
		plt.show()



	def OnListItemRightClick(self,event) :
		text=event.GetText()
		menu=wx.Menu()
		item=wx.MenuItem(menu,wx.ID_ANY,"查看曲线")
		menu.Append(item)
		self.PopupMenu(menu)#弹出右键菜单
		self.Bind(wx.EVT_MENU,self.PlotData(text),item)#不能将这一行放在item=wx.MenuItem(menu,wx.ID_ANY,"查看曲线")之后，这样会导致item不起作用
		menu.Destroy()

	def OnChecked(self,event) :
		box_linked=event.GetEventObject()
		label=box_linked.GetLabel()
		#关系对应字典
		relation={
			"开盘价":'open',
			"收盘价":'close',
			"最高价":'high',
			"最低价":'low',
			"交易总量":'volume'
		}
		self.OptionList[relation.get(label)]=box_linked.GetValue()

	def OnQuit(self,event):
		'''
			退出
		'''
		self.Close()
		self.Destroy()

	def createHeader(self) :
		self.list_ctrl.InsertColumn(0,'Symbol')
		self.list_ctrl.InsertColumn(1,'Name')
		self.list_ctrl.InsertColumn(2,'Price')
		self.list_ctrl.InsertColumn(3,'Change')
		self.list_ctrl.InsertColumn(4,'%Change')
		self.list_ctrl.InsertColumn(5,'Volume')
		self.list_ctrl.InsertColumn(6,'YTD Change')

	def OnRefresh(self,event) :
		thread_refresh=threading.Thread(target=self.insert_data)
		thread_refresh.start()
		#如果加上下面一句join方法会导致程序卡死
		# thread_refresh.join()

		#用_thread模块实现
		# thread.start_new_thread(self.insert_data, ())

	def insert_data(self) :
		self.list_ctrl.ClearAll()
		self.createHeader()
		data_list=rd.get_code_list()
		for data in data_list:
			self.list_index=self.list_ctrl.InsertItem(self.list_index+1,data[0])
			self.list_ctrl.SetItem(self.list_index,1,data[1])
			self.list_ctrl.SetItem(self.list_index,2,data[2])
			self.list_ctrl.SetItem(self.list_index,3,data[3])
			self.list_ctrl.SetItem(self.list_index,4,data[4])
			self.list_ctrl.SetItem(self.list_index,5,data[5])
			self.list_ctrl.SetItem(self.list_index,6,data[6])

			if self.list_index%2==0 :
				'''
					行颜色间隔变换
				'''
				self.list_ctrl.SetItemBackgroundColour(self.list_index,(134,225,249))
