#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  


header={'Cookie':'_jzqx=1.1487911215.1488114539.4.jzqsr=chinesean%2Ecom|jzqct=/affiliate/click%2Edo.jzqsr=votebar%2Ecom|jzqct=/user/survey/default%2Easpx; \
				  ASP.NET_SessionId=atznnab2gridqlsbmg5fys0w; \
				  Hm_lvt_958467b91507f9cc4a6a3a181102daa4=1488164634,1488165760,1488166451,1488188358; \
				  Hm_lpvt_958467b91507f9cc4a6a3a181102daa4=1488189602; \
				  _qzja=1.384597522.1487911214748.1488166450924.1488188358474.1488188358474.1488189602237..1.0.91.19; \
				  _qzjb=1.1488188358474.2.0.0.1.1; \
				  _qzjc=1; \
				  _qzjto=18.13.0; \
				  _jzqckmp=1; \
				  _jzqa=1.1478124577756892000.1487911215.1488166451.1488188358.19; \
				  _jzqc=1; \
				  _jzqb=1.4.10.1488188358.1'\
}

def download_image(url):
	req = urllib.request.Request(url, headers=header)
	with urllib.request.urlopen(req) as response:
		image = response.read()
	with open('F:\\python\\votebar.com\\verification_code.gif','wb') as f:
		f.write(image)



g_adsl_account = {"name": "宽带连接",
                "username": "15062114925",
                "password": "670110"}
 
     
class Adsl(object):
	#==============================================================================
	# __init__ : name: adsl名称
	#==============================================================================
	def __init__(self):
		self.name = g_adsl_account["name"]
		self.username = g_adsl_account["username"]
		self.password = g_adsl_account["password"]

	 
	#==============================================================================
	# set_adsl : 修改adsl设置
	#==============================================================================
	def set_adsl(self, account):
		self.name = account["name"]
		self.username = account["username"]
		self.password = account["password"]


	#==============================================================================
	# connect : 宽带拨号
	#==============================================================================
	def connect(self):
		cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
		os.system(cmd_str)
		time.sleep(5)

	 
	#==============================================================================
	# disconnect : 断开宽带连接
	#==============================================================================
	def disconnect(self):
		cmd_str = "rasdial %s /disconnect" % self.name
		os.system(cmd_str)
		time.sleep(5)


	#==============================================================================
	# reconnect : 重新进行拨号
	#==============================================================================
	def reconnect(self):
		self.disconnect()
		self.connect()


from datetime import *
import time
def Process(url,n):
	minSpan = 10.0
	maxSpan = 0.0
	sumSpan= 0.0
	over1s = 0
	proxy_support = urllib.request.ProxyHandler({'http':'115.28.168.247:80'})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	for i in range(n):
		startTime = datetime.now()
		try:
			res = urllib.request.urlopen(url,timeout=10)
		except:
			pass
		endTime = datetime.now()
		span = (endTime-startTime).total_seconds()
		sumSpan = sumSpan + span
		if span < minSpan:
			minSpan = span
		if span > maxSpan:
			maxSpan = span
		#超过一秒的
		if span>1:
			over1s=over1s + 1
		print(u'%s Spent :%s seconds'%(url,span))
	print(u'requested:%s times,Total Spent:%s seconds,avg:%s seconds, max:%s seconds,min:%s seconds,over 1 secnod:%s times'%(n,sumSpan,sumSpan/n,maxSpan,minSpan,over1s))
	print('\n')
  


if __name__ == '__main__':
	'''
	Process('http://www.votebar.com',100)
	'''
	driver = webdriver.Firefox()
	path=driver.firefox_profile.path
	print(path)
	
	'''
	l=Adsl()
	l.connect()
	'''
	'''
	download_image('http://www.votebar.com/user/RandomCodeImage.aspx')

	
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.get('http://www.votebar.com/r.aspx?r=54125726074462')
	print(driver.get_cookies())
	for cookie in driver.get_cookies():  
		print("%s:%s" % (cookie['name'], cookie['value']))
	'''
	'''
	profile = webdriver.FirefoxProfile()
	profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。
	profile.set_preference("network.proxy.http", "139.196.141.106")
	profile.set_preference("network.proxy.http_port", '28080')
	profile.update_preferences()
	browser = webdriver.Firefox(profile)
	browser.get("http://www.votebar.com/r.aspx?r=54125726074462")
	'''
	'''
	driver0 = webdriver.Firefox().get('http://www.baidu.com')
	driver1 = webdriver.Firefox().get('http://www.baidu.com')
	driver2 = webdriver.Firefox().get('http://www.baidu.com')
	driver3 = webdriver.Firefox().get('http://www.baidu.com')
	driver4 = webdriver.Firefox().get('http://www.baidu.com')
	driver5 = webdriver.Firefox().get('http://www.baidu.com')
	driver6 = webdriver.Firefox().get('http://www.baidu.com')
	driver7 = webdriver.Firefox().get('http://www.baidu.com')
	driver8 = webdriver.Firefox().get('http://www.baidu.com')
	driver9 = webdriver.Firefox().get('http://www.baidu.com')
	'''
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	