# -*- coding:UTF-8 -*-
#! /usr/bin/python3

from adsl import Adsl
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

from SQLite import get_ip_list,add_ip,update_questionnaire,get_account
import urllib.request
import re

def ip():
	text=urllib.request.urlopen("http://txt.go.sohu.com/ip/soip").read().decode("utf8")
	ip=re.search(r'.+"(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})".+',text)
	return ip.group(1)

def test_change_ip(questionnaire):
	while True:
		IP=ip()
		print('正在检测当前ip%s地址是否用过......'%IP)
		if not IP in get_ip_list(questionnaire):
			print('当前ip地址:%s可用'%IP)
			add_ip(questionnaire,IP)
			break
		else:
			print('%s已用过！'%IP)
			#a=Adsl()
			#a.reconnect()

def test_account(driver,url):
	driver.implicitly_wait(30)
	now_url=driver.current_url
	if now_url==url:
		raise AccountError('account无效！')
	else:
		u=re.search(r'http://project\.1diaocha\.com/survey/start\.aspx\?account=(\w+)&qquid=(\w+)',now_url)
		if u==None:
			raise QustionnaireError('已经参加过此次调查！')
		else:
			print('可以参加调查问卷！')

def complete_actions(driver):
	#开始进入调查页面
	driver.implicitly_wait(30)
	WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Button1"]'))).click()
	#选择第二个选项
	driver.implicitly_wait(30)
	WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="53998123975901_chk_2"]'))).click()
	#下一页
	driver.implicitly_wait(30)
	WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_ContentPlaceHolderButton_btnNext"]'))).click()
	#下一页
	driver.implicitly_wait(30)
	WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_ContentPlaceHolderButton_btnNext"]'))).click()	
	#下一页
	driver.implicitly_wait(30)
	WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_ContentPlaceHolderButton_btnNext"]'))).click()	
	#等待结束
	driver.implicitly_wait(30)

class AccountError(Exception):
	pass

class QustionnaireError(Exception):
	pass
		
def complete(account,questionnaire):
	print('1.开始检测ip地址')
	test_change_ip(questionnaire)
	url='http://project.1diaocha.com/survey/default.aspx?account=%s&temp=%s'%(account,questionnaire)
	print('2.打开浏览器')
	driver = webdriver.Firefox()
	driver.maximize_window()
	driver.get(url)
	try:
		print('3.检测账户')
		test_account(driver,url)
		print('4.开始作答')
		complete_actions(driver)
		print('5.更新数据库')
		update_questionnaire(account,questionnaire)
	except AccountError as e:
		update_questionnaire(account,'0')
		print(e)
	except QustionnaireError as e:
		#update_questionnaire(account,'1')
		print(e)
	except Exception as e:
		print(e)
	print('6.关闭浏览器')
	driver.quit()
	

class complete1(object):
	def __init__(self,proxy,account,quid):
		proxy=proxy.split(':')
		self.__ip=proxy[0]
		self.__port=int(proxy[1])
		#self.__qurl='http://project.1diaocha.com/survey/default.aspx?account=%s&temp=%s'%(account,quid)
		self.__qurl='http://www.ip138.com/'
	
	def start_browser(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference('network.proxy.type', 1)
		profile.set_preference("network.proxy.http", self.__ip)
		profile.set_preference("network.proxy.http_port", self.__port)
		profile.set_preference("network.proxy.socks", self.__ip)
		profile.set_preference("network.proxy.socks_port", self.__port)
		profile.set_preference("network.proxy.ftp", self.__ip)
		profile.set_preference("network.proxy.ftp_port", self.__port)
		profile.set_preference("network.proxy.ssl", self.__ip)
		profile.set_preference("network.proxy.ssl_port", self.__port)	
		profile.update_preferences()
		self.__driver = webdriver.Firefox(profile)
		self.__driver.get(self.__qurl)		

		
if __name__ == '__main__':
	questionnaire='038ceeb25a358ea0'
	while True:
		account=get_account()
		if account=='':
			break
		complete(account,questionnaire)
		print('  ')
	print('完成！')
	
	
	
	
