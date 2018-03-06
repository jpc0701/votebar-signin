#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time


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
		while True:
			exit_code = os.system('ping www.baidu.com')
			if not exit_code:
				break
	 
	#==============================================================================
	# disconnect : 断开宽带连接
	#==============================================================================
	def disconnect(self):
		cmd_str = "rasdial %s /disconnect" % self.name
		os.system(cmd_str)
		while True:
			exit_code = os.system('ping www.baidu.com')
			if exit_code:
				break


	#==============================================================================
	# reconnect : 重新进行拨号
	#==============================================================================
	def reconnect(self):
		self.disconnect()
		self.connect()

		
if __name__ == '__main__':
	a=Adsl()
	a.reconnect()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	