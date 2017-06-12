#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09
# @Author  : Bob Liao (codechaser1@gmail.com)
# @Link    : https://github.com/coderchaser
# @Version : python3.4

#创建大小写转换字典
num_dic={
	# 1 : "壹",
	# 2 : "贰",
	# 3 : "叁",
	# 4 : "肆",
	# 5 : "伍",
	# 6 : "陆",
	# 7 : "柒",
	# 8 : "捌",
	# 9 : "玖",
	# 0 : "零"
	u"1": u"壹",
	u"2": u"贰",
	u"3": u"叁",
	u"4": u"肆",
	u"5": u"伍",
	u"6": u"陆",
	u"7": u"柒",
	u"8": u"捌",
	u"9": u"玖",
	u"0": u"零"
}
#将输入金额分组，从最低位开始四位分组，最后一组可以少于四位
def group(num_str) :
	group_list=[]
	i=len(num_str)
	while i>=4 :
		group_list.append(num_str[i-4:i])
		i-=4
	if i!=0 :
		group_list.append(num_str[:i])
	#保证顺序输出
	group_list.reverse()
	return group_list
#原始读函数,数字必须全部转化为字符串
def read_four(num_four) :
	#读四位分组
	gewei=""
	shiwei=""
	baiwei=""
	qianwei=""
	num_len=len(num_four)
	#当传入的数字为0000时num_len会变成1，会发生list越界
	if num_four[-1]!=u'0' :
		if num_four[-2]!=u'0' :
			gewei=num_dic[num_four[-1]]
		else :
			gewei=u"零"+num_dic[num_four[-1]]
	if num_four[-2]!=u'0' :
		if num_four[-3]!=u'0' :
			shiwei=num_dic[num_four[-2]]+u"拾"
		else :
			shiwei=u"零"+num_dic[num_four[-2]]+u"拾"
	if num_four[-3]!=u'0' :
		if num_four[-4]!=u'0' :
			baiwei=num_dic[num_four[-3]]+u"佰"
		else :
			baiwei=u"零"+num_dic[num_four[-3]]+u"佰"
	if num_four[-4]!=u'0' :
		qianwei=num_dic[num_four[-4]]+u"仟"
	return qianwei+baiwei+shiwei+gewei
def read_three(num_three) :
	#读三位分组
	gewei=""
	shiwei=""
	baiwei=""
	if num_three[-1]!=u'0' :
		if num_three[-2]!=u'0' :
			gewei=num_dic[num_three[-1]]
		else :
			gewei=u"零"+num_dic[num_three[-1]]
	if num_three[-2]!=u'0' :
		if num_three[-3]!=u'0' :
			shiwei=num_dic[num_three[-2]]+u"拾"
		else :
			shiwei=u"零"+num_dic[num_three[-2]]+u"拾"
	if num_three[-3]!=u'0' :
		baiwei=num_dic[num_three[-3]]+u"佰"
	return baiwei+shiwei+gewei
def read_two(num_two) :
	#读二位分组
	gewei=""
	shiwei=""
	if num_two[-1]!=u'0' :
		if num_two[-2]!=u'0' :
			gewei=num_dic[num_two[-1]]
		else :
			gewei=u"零"+num_dic[num_two[-1]]
	if num_two[-2]!=u'0' :
		if num_two[-2] ==u'1' :
			shiwei=u"拾"
		else :
			shiwei=num_dic[num_two[-2]]+u"拾"
	return shiwei+gewei
def read_one(num_one) :
	#读一位分组
	if num_one!=u'0' :
		return num_dic[num_one]
	else :
		return ""
#建立调用字典关系
call_read={
	1 : read_one,
	2 : read_two,
	3 : read_three,
	4 : read_four
}
def read(num) :
	#将数字int转化为字符串
	#金额不可以像如下形式：
	#		0100
	#Python3会将0开头的数字
	#识别为8进制，一般人不会
	#这样写金额，不予考虑
	num_str=str(abs(num))
	#分组
	group_list=group(num_str)
	read_part=[]
	if num<0 :
		read_part.append(u'负')
	for i in group_list :
		len_part=len(i)
		read_part.append(call_read[len_part](i))
		if group_list.index(i)== 0 and len(group_list)>1 :
			read_part.append(u'万')
	read_part.append(u'圆')
	print("".join(read_part))

# num=int(input('Your Number: '))
# print(num)
read(90901001)