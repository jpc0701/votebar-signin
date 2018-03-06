# -*- coding:UTF-8 -*-
#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

class login():
	def __init__(self,username,proxy=''):
		self.__username=username
		self.__password='jpc19930701'
		if proxy=='':
			self.__driver = webdriver.Firefox()
		else:
			proxy=proxy.split(':')
			print(proxy[0])
			print(proxy[1])
			profile = webdriver.FirefoxProfile()
			profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。
			profile.set_preference("network.proxy.http", proxy[0])
			profile.set_preference("network.proxy.http_port", proxy[1])
			profile.update_preferences()
			self.__driver = webdriver.Firefox(profile)
		self.__driver.implicitly_wait(30)
		self.__driver.maximize_window()
		self.__driver.get('http://www.votebar.com/')
		username_input=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtEmail"]')))
		username_input.clear()
		username_input.send_keys(self.__username)
		password_input=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtPassword"]')))
		password_input.clear()
		password_input.send_keys(self.__password)		
		WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="btnLogin"]'))).click()
		
	def driver_quit(self):
		self.__driver.quit()
		
if __name__ == '__main__':
	l=login('chi49106752@sohu.com')



