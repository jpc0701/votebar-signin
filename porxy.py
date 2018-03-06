#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote
import urllib.request
import socket
import time
import re

def Proxy_IP(area='',order_code='2581208584509842',num='1',area_type='1',ports='',nports='',scheme='',anonymity=3,order='3',style='3'):
	'''
	order_code:订单号
	num:返回IP的数量
	area_type:地区，1-大陆，2-港澳台，3-国外,空值代表任意
	area:地区，如果是国内的填写地级市，港澳台填写香港、澳门或者台湾，国外的就填哪个国家
	port:端口,空值-任意
	nports:反选端口（排除端口），1-是，空值-否
	scheme:类型，空值-HTTP,1-HTTPS
	anonymity:匿名度，空值-任意，1-透明代理，2-普通代理，3-高匿代理
	order：排序方式，1-按最后检测时间（近-远），2-按存活率（大-小），3-按响应速度（快-慢）
	style:返回格式，空值-默认，1-空格，2-\n,3-\r\n
	
	此次只可修改订单号、返回数量、地区和匿名度
	'''
	area=quote(area)
	url='http://%s.standard.hutoudaili.com/?num=%s&area_type=1&area=%s&anonymity=%s&style=1&order=3'%(order_code,num,area,str(anonymity))
	times=0
	while True:
		time.sleep(5)
		times+=1
		try:
			with urllib.request.urlopen(url) as response:
				IP = response.read().decode('utf-8').strip()
		except:
			return '网络发生错误'
		
		if IP != '没有相关数据':
			return IP.replace('\r\n','')
			'''
			try:
				print(IP)
				timeout = 5
				socket.setdefaulttimeout(timeout)
				proxy_support = urllib.request.ProxyHandler({'http':'121.42.244.14:3128'})
				opener = urllib.request.build_opener(proxy_support)
				urllib.request.install_opener(opener)
				a = urllib.request.urlopen("http://www.votebar.com").read().decode("utf8")
				print(a)
				return IP
			except:
				print ('下一轮获取IP')
			'''
		else:
			if times>=3:
				times=0
				if anonymity==3:
					anonymity-=1
					url='http://%s.standard.hutoudaili.com/?num=%s&area_type=1&area=%s&anonymity=%s&style=1&order=3'%(order_code,num,area,str(anonymity))
				elif anonymity==2:
					url='http://%s.standard.hutoudaili.com/?num=1&area_type=1&anonymity=3&style=1&order=3'%order_code
				else:
					return '无法获取满足条件的代理IP，或许是因为网络原因！'
		







if __name__ == '__main__':
	print(Proxy_IP('南京'))


















