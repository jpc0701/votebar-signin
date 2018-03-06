# -*- coding:UTF-8 -*-
#! /usr/bin/python3

import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from random import randint
from persons import Person
from ysdm import APIClient
from PIL import Image
from SQLite import Insert


login_url='http://www.votebar.com/r.aspx?r=54125726074462'
login_password='jpc19930701'

'''
def download_image(url):
	with urllib.request.urlopen(url) as response:
		image = response.read()
	with open('F:\\python\\votebar.com\\verification_code.gif','wb') as f:
		f.write(image)
'''

class signin():
	def __init__(self,email_user,email_pass,proxy=''):
		self.__email_user=email_user
		self.__email_pass=email_pass
		self.__person=Person()
		if proxy=='':
			self.__driver = webdriver.Firefox()
		else:
			proxy=proxy.split(':')
			print(proxy[0])
			print(proxy[1])
			profile = webdriver.FirefoxProfile()
			profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。
			profile.set_preference("network.proxy.http", proxy[0])
			profile.set_preference("network.proxy.http_port", int(proxy[1]))
			profile.set_preference("network.proxy.socks", proxy[0])
			profile.set_preference("network.proxy.socks_port", int(proxy[1]))
			profile.set_preference("network.proxy.ftp", proxy[0])
			profile.set_preference("network.proxy.ftp_port", int(proxy[1]))
			profile.set_preference("network.proxy.ssl", proxy[0])
			profile.set_preference("network.proxy.ssl_port", int(proxy[1]))	
			profile.update_preferences()
			self.__driver = webdriver.Firefox(profile)
		self.__driver.implicitly_wait(30)
		self.__driver.maximize_window()
		self.__driver.get(login_url)
		self.__driver.implicitly_wait(30)
		self.fill_login_info()
		#self.start_login()
		
	def download_image(self):	
		self.__driver.save_screenshot('screenshot.png')
		element=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="i1"]')))
		left = element.location['x']
		top = element.location['y']
		right = element.location['x'] + element.size['width']
		bottom = element.location['y'] + element.size['height']
		im = Image.open('screenshot.png') 
		im = im.crop((left, top, right, bottom))
		im.save('verification_code.png')
	
	def fill_login_info(self):
		WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtEmail"]'))).send_keys(self.__email_user)
		WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtPassword"]'))).send_keys(login_password)
		WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtConfirmPassword"]'))).send_keys(login_password)
		WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtName"]'))).send_keys(self.__person.info()['name'])
		if self.__person.info()['sex']=='男':
			WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rdoBoy"]'))).click()
		else:
			WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rdoGirl"]'))).click()
		
		self.select_option('//*[@id="dropYear"]',self.__person.info()['birthday_y'])
		self.select_option('//*[@id="dropMonth"]',self.__person.info()['birthday_m'])
		self.select_option('//*[@id="dropDay"]',self.__person.info()['birthday_d'])
		self.select_option('//*[@id="selCountry"]','中国')
		self.select_option('//*[@id="selProvincial"]',self.__person.info()['address_province'])
		self.select_option('//*[@id="selCity"]',self.__person.info()['address_city'])
		district=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selAreaInfo"]')))
		while True:
			if len(Select(district).options)>=2:
				break
		Select(district).select_by_index(randint(1,len(Select(district).options)-1))
		
	def select_option(self,select_xpath,text):
		if text.startswith('0'):
			text=text.replace('0','')
		temp_select=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,select_xpath)))
		Select(temp_select).select_by_visible_text(text)
		
	def start_login(self):
		while True:
			self.download_image()
			client = APIClient('verification_code.png')
			code=client.upload_image()
			WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtuvalidate"]'))).clear()
			WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtuvalidate"]'))).send_keys(code)
			flag=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="lblmsg8"]')))
			flag.click()
			time.sleep(0.5)
			if flag.get_attribute('class')=='note_ok':
				break
			else:
				flag=WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="i1"]'))).click()
				client.error_submit()
				time.sleep(1)
		WebDriverWait(self.__driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="BtnRegister"]'))).click()
		#time.sleep(3)
		WebDriverWait(self.__driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/a'))).click()
		Insert('VOTEBAR',['USERNAME', \
						  'PASSWORD', \
						  'NAME', \
						  'BIRTHDAY', \
						  'SEX', \
						  'ADDRESS', \
						  'ACTIVATION'], \
						 [self.__email_user, \
						 login_password, \
						 self.__person.info()['name'], \
						 self.__person.info()['birthday'], \
						 self.__person.info()['sex'], \
						 self.__person.info()['address'], \
						 0])
		print('完成')
	
	def return_driver(self):
		return self.__driver
	
	def return_name(self):
		return self.__person.info()['name']
		
if __name__ == '__main__':
	l=signin('jiexian4982316@sohu.com','panguijiongzhuo')
	
	
	
	
	
	
	