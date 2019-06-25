# -*- coding: utf-8 -*-
import os

def h(a):
	result = "";
	for i in range(a):
		result+="#"
	return result+" "

def create_template():
	filename = raw_input("请输入文件名称：")
	totalname = filename + ".md"
	if(os.path.exists(totalname)):
		print "创建失败，文件已存在"
		return
	
	with open(totalname,"w") as f:
		method = input("请输入代码实现种数")

		f.write(h(1)+"["+filename+"]"+"[title]"+"\n")
		f.write(h(2)+"题目描述"+"\n")
		f.write(h(2)+"思路"+"\n")
		if method>1:
			for i in range(method):
				f.write(h(6)+"法"+str(i+1)+":"+"\n")
		f.write(h(2)+"代码实现"+"\n")
		
		for i in range(method):
			f.write("```java\n```\n")

		link = raw_input("请输入url：")
		f.write("[title]:"+link+"\n")

create_template()
