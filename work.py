#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  



from activation_link import ActEmail
from votebar_signin import signin
from votebar_login import login
from SQLite import unregister_email,get_noaccount,Delete,Update
from votebar_activation import activation
from adsl import Adsl
import shutil
import time
import os
import re
	
def update_account():
	while True:
		em=get_noaccount()
		if em=={}:
			break
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get('http://www.votebar.com/')
		WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtEmail"]'))).send_keys(em['username'])
		WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtPassword"]'))).send_keys(em['password'])
		WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="btnLogin"]'))).click()
		driver.implicitly_wait(30)
		if driver.current_url=='http://www.votebar.com/':
			Delete('VOTEBAR','USERNAME',em['username'])
			print('此账号不存在，已删除！')
			driver.quit()
			continue
		driver.switch_to_frame("SurveyDisplay")
		try:
			temp_url=WebDriverWait(driver,15,0.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#QQSurvey1 a')))[0].get_attribute('href')
			temp=re.search(r'.+account=(\w+)&.+',temp_url)
			if temp !=None:
				account=temp.group(1)
				print('获取account:%s'%account)
				Update('VOTEBAR','ACCOUNTID',account,em['username'])
		except Exception as e:
			print(e)
			print('无法获取account！')
		finally:
			driver.quit()
		
		

def work():
	a=Adsl()
	counts=0
	while True:
		try:
			#if counts>=10:
			#	counts=0
			#	a.reconnect()
			em=unregister_email()
			if em=={}:
				break
			l=signin(em['email'],em['password'])
			driver=l.return_driver()
			l.start_login()
			driver=activation(l.return_driver(),em['email'],l.return_name())
			#path=driver.firefox_profile.path
			driver.quit()	
			#shutil.rmtree(path)
			counts+=1
		except UnexpectedAlertPresentException as e:
			driver.quit()
			a.reconnect()	
		except Exception as e:
			print(e)
			break					
	print('123')	
		
if __name__ == '__main__':
	#work()
	update_account()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		