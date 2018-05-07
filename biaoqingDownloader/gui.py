#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-01 10:10:58
# @Author  : Bob Liao (codechaser@163.com)
# @Link    : https://github.com/coderchaser


import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import webbrowser as wb
import re
import threading
import os
import downloader



class Application(tk.Frame) :
	def __init__(self,master = None) :
		super(Application,self).__init__(master)
		self.pack()
		self.__create_widgets()


	def __create_widgets(self) :

		#标签，介绍用
		self.__label=tk.Label(self,text="可输入多个关键词查询，请以逗号隔开。\n可以在最后指定下载数量，默认为100",justify=tk.LEFT)
		self.__label.pack(side=tk.TOP,pady=10)

		#关键词输入框
		self.__keywords_entry = tk.Entry(self,width=30)
		self.__keywords_entry.pack()
		self.__keywords = tk.StringVar(self,value="关键词1，关键词2，···，100")
		self.__keywords_entry["textvariable"]=self.__keywords
		self.__keywords_entry.bind('<Key-Return>',self.download)


		frame=tk.Frame(self)

		#下载目录按钮
		self.__open_dir=tk.Button(frame,text="打开下载目录",command=self.__open_folder)
		self.__open_dir.grid(in_=frame,row=0,padx=10)
		#下载按钮
		self.__download_button=tk.Button(frame,text="下载",command=self.__download)

		self.__download_button.grid(in_=frame,row=0,column=1)

		frame.pack()

		#进度条
		self.__progress_bar = ttk.Progressbar(self,orient="horizontal",mode="determinate",length=200)
		# self.__progress_bar.pack()
		# self.__progress_bar.start()


		#致谢
		self.__thank_label=tk.Label(self,text="下载表情包图片所用API来自:")
		self.__thank_label.pack()
		self.__api_label=tk.Label(self,text="https://www.doutula.com/apidoc",fg="blue",cursor="target")
		self.__api_label.pack()
		self.__api_label.bind("<Button-1>",self.__label_clicked)

	def download(self,event) :
		thread_=threading.Thread(target=self.download_image,args=[self.__keywords.get()])
		thread_.setDaemon(True)
		thread_.start()


	def __download(self) :
		self.download(None)


	def download_image(self,key_words_list) :

		self.__progress_bar.pack()
		self.__progress_bar["value"]=0
		# self.__
		key_words=re.split(r"[,，]",key_words_list)
		if not key_words or '···' in key_words :
			messagebox.showinfo("提示","请确认关键词输入正确!")
			return

		try:
			number = int(key_words[-1])
		except ValueError as e:
			number = 100

		total_number = len(key_words[:-1]) * number;

		
		
		for key_word in key_words[:-1] :
			if key_words.index(key_word) == 0:
				initTotalCount = True
			else:
				initTotalCount = False
			dirpath='./tmp/'+key_word
			image_downloader = downloader.Downloader(number,key_word,0,dirpath,False,progressBar=self.__progress_bar,totalNumber=total_number,initTotalCount=initTotalCount)
			image_downloader.run()

		messagebox.showinfo("搞定","图片已下载完毕！点击下载目录按钮可直接打开文件夹")
		downloader.Downloader.totalNumber = 0

		# self.__progress_bar.stop()


		



		

	def __label_clicked(self,event) :
		url=self.__api_label["text"]
		wb.open_new(url)

	
	
	def __open_folder(self) :
		try:
			os.startfile(r".\tmp")
		except Exception as e:
			messagebox.showerror("错误","你还没有下载过图片哦！")


if __name__ == '__main__':
	root = tk.Tk()
	root.title("表情包下载器")
	root_width = 300;root_height = 200
	root.geometry("%dx%d+%d+%d" %(root_width,root_height,(root.winfo_screenwidth()-root_width)/2,(root.winfo_screenheight()-root_height)/2))
	root.resizable(False,False)
	myApp = Application(master=root)

	myApp.mainloop()
