#! usr/bin/env python3
# coding :utf-8


"""
@version: ??
@author: Bob Liao
@liscense: BSD
@contact: codechaser1@gmail.com
@site: https://github.com/coderchaser
@time: 2017/6/1 23:00
"""

#写入html
class HtmlOutputer() :
	def __init__(self):
		self.datas=[]
	
	def collect_data(self,data) :
		if data is None :
			return
		self.datas.append(data)
	def output_html(self) :
		with open('output.html','w',encoding='utf-8') as fout :
			fout.write('<!DOCTYPE html>')
			fout.write('<html>')
			fout.write('<body>')
			fout.write('<table>')
			for data in self.datas:
				fout.write('<tr>')
				fout.write('<td>%s</td>' % data['url'])
				fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
				fout.write('<td>%s</td>' % data['summary'].encode("utf-8"))
				fout.write('</tr>')
			fout.write('</table>')
			fout.write('</body>')
			fout.write('</html>')
