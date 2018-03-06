# -*- coding:UTF-8 -*-
#! /usr/bin/python3

import re
import time 
import sqlite3
from SQLite import Update
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from activation_link import ActEmail

def activation(driver,email,name):
	while True:
		try:
			Alert(driver).accept()
			break
		except:
			print('等待中......')
	driver.switch_to_frame("SurveyDisplay")
	
	try:
		temp_url=WebDriverWait(driver,15,0.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#QQSurvey1 a')))[0].get_attribute('href')
		temp=re.search(r'.+account=(\w+)&.+',temp_url)
		if temp !=None:
			account=temp.group(1)
			Update('VOTEBAR','ACCOUNTID',account,email)
	except:
		print('没有获得account！')
	
	driver.switch_to.default_content()
	c=0
	while True:
		activation_link='http://www.votebar.com/User/EmailSuccessful.aspx?uaccount=%s&uemail=%s'%(name,email)
		driver.get(activation_link)
		info=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="labinfo"]'))).text
		#if info.strip() =='恭喜您激活邮箱成功，获得50钻石奖励！':
		if info.strip() !='该邮箱不存在!':
			Update('VOTEBAR','ACTIVATION',1,email)
			print('已激活！')
			break
		time.sleep(1)
		'''
		c+=1
		if c>=10:
			Update('VOTEBAR','ACTIVATION',0,email)
			print('激活失败！请手动完成激活！')
			break
		Activation=ActEmail(email,password,'smtp.sohu.com')
		activation_link=Activation.get_activation_link()
		if activation_link!=None:
			driver.get(activation_link)
			time.sleep(1)
			Update('VOTEBAR','ACTIVATION',1,email)
			print('已激活！')
			break
		time.sleep(5)
		'''
	return driver
#	driver.quit()

def only_activation():
	conn = sqlite3.connect('test.db')
	cursor = conn.execute("SELECT USERNAME,NAME FROM VOTEBAR_NONACTIVATED")
	l=[]
	for em in cursor:
		j={}
		j['email']=em[0]
		j['name']=em[1]
		l.append(j)
	conn.close()
	driver = webdriver.Firefox()
	for i in l:
		email=i['email']
		name=i['name']
		driver.get('http://www.votebar.com/User/EmailSuccessful.aspx?uaccount=%s&uemail=%s'%(name,email))
		Update('VOTEBAR','ACTIVATION',1,email)
		print('已激活！')
		time.sleep(1)
	
if __name__ == '__main__':
	only_activation()