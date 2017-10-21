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


class MyFrame(wx.Frame) :
	def __init__(self,title) :
		super(MyFrame,self).__init__(None,title=title,size=(400,600))
		self.CreateStatusBar()
		# self.Center()
		self.InitUI()

	def InitUI(self) :
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
		code_label=wx.StaticText(panel,label='Stock Code: ')
		hboxsizer.Add(code_label,0,wx.ALIGN_BOTTOM)
		code_text=wx.TextCtrl(panel,value='BA',style=wx.TE_PROCESS_ENTER)
		#TODO: 
		hboxsizer.Add(code_text)
		sizer.Add(hboxsizer)
		panel.SetSizer(sizer)

	def menuhandler(self,event) :
		#TODO:add a handler of save image

		id=event.GetId()
		print(id,"Pressed!")

	def OnQuit(self,event):
		self.Close()

app=wx.App()
a=MyFrame('Stock')
a.Show(True)
app.MainLoop()