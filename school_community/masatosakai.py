
#!/usr/bin/env/python3
# -*- coding:utf8 -*-


# *.webp ---> *.PNG
# source web: Douban

import requests
import os
import re
import threading
from PIL import Image
from bs4 import BeautifulSoup


LINK_POOL=set()
def get_link(url) :
	init_page=requests.get(url)
	rq=init_page.text
	soup_=BeautifulSoup(rq,"html.parser")
	for image_ in soup_.findAll(name="img",attrs={"src":re.compile(r"https://img\d.doubanio.com/view/photo/m/public/*.*")}) :
		if not image_.src in LINK_POOL :
			LINK_POOL.add(image_["src"])
	hasNext=soup_.find(name="a",text="后页>")
	if hasNext :
		get_link(hasNext["href"])

def download_picture(url,path,name) :
	rq=requests.get(url,timeout=10)
	if rq.status_code==200 :
		path_=".\\"+path+"\\"+name
		print(path_)
		with open(path_,"wb") as f:
			f.write(rq.content)

get_link("https://movie.douban.com/celebrity/1028795/photos/")
dirname="MasatoSakai"
if not os.path.exists(dirname) :
	os.mkdir(dirname)
i=0
for link in LINK_POOL :
	name=dirname+"{0}.jpg".format(i)
	t=threading.Thread(target=download_picture,args=(link,dirname,name))
	i+=1
	t.start()
	t.join()