#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-10-20 21:55:29
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\sublimeText\hipython_cousera\news_title\main.py


import gui_wx
import wx

app=wx.App()
frame=gui_wx.MyFrame('Stock')
frame.Show(True)
app.MainLoop()