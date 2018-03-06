#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

import os
from PIL import Image

def download_image(n):	
	for i in range(n):
		driver = webdriver.Firefox()
		#driver =  webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\Python35\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe')
		#driver.maximize_window()
		driver.set_window_size(1380,768)
		driver.get('http://www.votebar.com/Reg.html')
		driver.implicitly_wait(30)
		driver.save_screenshot('screenshot1.png')
		element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="i1"]')))
		left = element.location['x']
		top = element.location['y']
		right = element.location['x'] + element.size['width']
		bottom = element.location['y'] + element.size['height']
		im = Image.open('screenshot1.png') 
		im = im.crop((left, top, right, bottom))
		#os.remove('screenshot1.png')
		im.save('%d.png'%i)
		driver.quit()
	
if __name__ == '__main__':
	download_image(1)