#! /usr/bin/env/python3
# encoding:utf-8

import codecs

with codecs.open('busan_node.txt','r',encoding='gbk') as f:
	with open('busan_node_tf.txt','w') as w:
		for line in f.readlines() :
			w.write(line+'\n')
