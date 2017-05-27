#!/usr/bin/env/python3
# coding:utf-8
#aythor:Bob Liao
#email:codechaser1@gmail.com
#practicing codes from https://www.shiyanlou.com/courses/677
#latest update on 2017-05-27 21:34
import os
import sys
import jieba
import codecs
import math
import jieba.posseg as pseg


class Busan(object) :
	def __init__(self,script_name,jieba_dict) :
		self.names={}
		self.relationships={}
		self.lineNames=[]
		self.script_name=script_name
		self.my_dict=jieba_dict
		self.getRelationships()
		self.constructNetwork()
		self.writeNode()

	def getRelationships(self) :
		jieba.load_userdict(self.my_dict)
		with codecs.open(self.script_name,mode='r',encoding='utf8') as f:
			for line in f.readlines() :
				poss=pseg.cut(line)
				self.lineNames.append([])
				for w in poss :
					if w.flag!='nr' or len(w.word)<2 :
						continue

					self.lineNames[-1].append(w.word)
					if self.names.get(w.word) is None :
						self.names[w.word]=0
						self.relationships[w.word]={}
					self.names[w.word]+=1
	def constructNetwork(self) :
		for line in self.lineNames :
			for name1 in line :
				for name2 in line :
					if name1==name2 :
						continue
					if self.relationships[name1].get(name2) is None :
						self.relationships[name1][name2]=1
					else :
						self.relationships[name1][name2]=self.relationships[name1][name2]+1
	def writeNode(self) :
		with codecs.open('fushanxing_node.txt','w',encoding='gbk') as f :
			f.write('Id Label Weight\r\n')
			for name,times in self.names.items() :
				f.write(name+' '+name+' '+str(times)+'\r\n')
		with codecs.open('fushanxing_edge.txt','w','gbk') as f :
			f.write('Source Target Weight\r\n')
			for name,edges in self.relationships.items() :
				for v,w in edges.items() :
					if w>3 :
						f.write(name+' '+v+' '+str(w)+'\r\n')

if __name__ == '__main__':
	Busan('script_of_fushanxing.txt','dict.txt')