#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-10-20 21:56:09
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\sublimeText\hipython_cousera\news_title\gui_wx.py


import pandas as pd
import wx
import threading
import retrieve_data as rd
import io

ID_LIST_CTRL=1234

class MyFrame(wx.Frame) :
	def __init__(self,title) :
		super(MyFrame,self).__init__(None,title=title,size=(600,600))
		self.CreateStatusBar()
		# self.Center()
		self.InitUI()

	def InitUI(self) :
		box_dict={
			"Open":True,
			"Close":True,
			"High":True,
			"Low":True,
			"Volume":True
		}
		io_string=open('stocks.png','rb')
		image=wx.Bitmap(wx.Image(io_string))
		icon_=wx.Icon()
		icon_.CopyFromBitmap(wx.Bitmap(image))
		self.SetIcon(icon_)

		self._menu=wx.MenuBar()
		filemenu=wx.Menu()
		save_menu=wx.MenuItem(filemenu,wx.ID_SAVE,text='保存')
		refresh_menu=wx.MenuItem(filemenu,wx.ID_REFRESH,'刷新')
		#TODO:add handlers
		self.Bind(wx.EVT_MENU,self.menuhandler)
		filemenu.Append(save_menu)
		filemenu.Append(refresh_menu)
		filemenu.Append(wx.ID_EXIT,'退出',"退出应用")
		self.Bind(wx.EVT_MENU,self.OnQuit,id=wx.ID_EXIT)
		self._menu.Append(filemenu,"File")
		self.SetMenuBar(self._menu)

		panel=wx.Panel(self)
		sizer=wx.BoxSizer(wx.VERTICAL)
		hboxsizer=wx.BoxSizer(wx.HORIZONTAL)
		code_label=wx.StaticText(panel,label='股票代码： ')
		hboxsizer.Add(code_label,0,wx.ALIGN_BOTTOM)
		code_text=wx.TextCtrl(panel,value='BA',style=wx.TE_PROCESS_ENTER)
		#TODO: add code_text handler
		hboxsizer.Add(code_text)

		checkboxSizer=wx.BoxSizer(wx.HORIZONTAL)
		for key,value in box_dict.items() :
			checkbox=wx.CheckBox(panel,label=key)
			checkbox.SetValue(value)
			checkboxSizer.Add(checkbox)
		self.Bind(wx.EVT_CHECKBOX,self.OnChecked)

		self.list_ctrl=wx.ListCtrl(panel,id=ID_LIST_CTRL,style=wx.LC_REPORT)
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
		self.insert_data()
		

		sizer.Add(hboxsizer,0,wx.ALL,5)
		sizer.Add(checkboxSizer,0,wx.ALL,5)
		sizer.Add(self.list_ctrl,-1,wx.ALL | wx.EXPAND,5)
		panel.SetSizer(sizer,wx.EXPAND |wx.ALL)

	def menuhandler(self,event) :
		#TODO:add a handler of save image

		id=event.GetId()
		print(id,"Pressed!")

	def OnChecked(self,event) :
		box_linked=event.GetEventObject()
		print(box_linked.GetValue())
		print(box_linked.GetLabel())

	def OnQuit(self,event):
		self.Close()

	def createHeader(self) :
		self.list_ctrl.InsertColumn(0,'Symbol')
		self.list_ctrl.InsertColumn(1,'Name')
		self.list_ctrl.InsertColumn(2,'Price')
		self.list_ctrl.InsertColumn(3,'Change')
		self.list_ctrl.InsertColumn(4,'%Change')
		self.list_ctrl.InsertColumn(5,'Volume')
		self.list_ctrl.InsertColumn(6,'YTD Change')

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
				self.list_ctrl.SetItemBackgroundColour(self.list_index,(134,225,249))

app=wx.App()
a=MyFrame('Stock')
a.Show(True)
app.MainLoop()