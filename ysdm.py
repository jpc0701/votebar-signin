#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
import urllib.request
import hashlib
import json
import os

class APIClient(object):
	def __init__(self,imagepath,username='******',password='*******',typeid='3050',timeout='90',softid='58981',softkey='a0fcc7c8fbcc4cfb84c06c71622198d3'):
		self.__param={}
		self.__param['username']=username
		self.__param['password']=password
		self.__param['typeid']=typeid
		self.__param['timeout']=timeout
		self.__param['softid']=softid
		self.__param['softkey']=softkey
		self.__param['id']=''
		self.__imagepath=imagepath
	
	def imagetobytes(self):
		with open(self.__imagepath,'rb') as image:
			return image.read()
	
	def upload_image(self):
		url='http://api.ysdm.net/create.json'
		timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		boundary = '------------' + hashlib.md5(timestr.encode()).hexdigest().lower()
		boundarystr = '\r\n--%s\r\n'%(boundary)

		bs = b''
		for key,value in self.__param.items():
			if key !='result_id':
				bs = bs + boundarystr.encode('ascii')
				param = "Content-Disposition: form-data; name=\"%s\"\r\n\r\n%s"%(key, value)
				#print param
				bs = bs + param.encode('utf8')
		bs = bs + boundarystr.encode('ascii')

		header = 'Content-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/gif\r\n\r\n'%('sample')
		bs = bs + header.encode('utf8')

		bs = bs + self.imagetobytes()
		tailer = '\r\n--%s--\r\n'%(boundary)
		bs = bs + tailer.encode('ascii')

		headers = {'Content-Type':'multipart/form-data; boundary=%s'%boundary,
					'Connection':'Keep-Alive',
					'Expect':'100-continue',
					}
		req = urllib.request.Request(url, bs, headers)
		with urllib.request.urlopen(req) as response:
			result_dic=json.loads(response.read().decode('utf-8'))
		if 'Result' in result_dic:
			self.__param['id']=result_dic['Id']
			return result_dic['Result']
		else:
			return 'Error!!!'

	def error_submit(self):
		url='http://api.ysdm.net/reporterror.json'

		bs = []
		for key,value in self.__param.items():
			if key=='username' or key=='password' or key=='softid' or key=='softkey' or key=='id':
				bs.append('%s=%s'%(key,value))
		bs='&'.join(bs)
		bs=bs.encode()
		req = urllib.request.Request(url, data=bs)
		with urllib.request.urlopen(req) as response:
			print(response.read().decode('utf-8'))
	
def download_image(url):
	with urllib.request.urlopen(url) as response:
		image = response.read()
	with open('F:\\python\\votebar.com\\verification_code.gif','wb') as f:
		f.write(image)
	
if __name__ == '__main__':

	client = APIClient(r'F:\python\votebar.com\1.png')
	print(client.upload_image())
	client.error_submit()
	'''
	download_image('http://www.votebar.com/user/RandomCodeImage.aspx?id=0.6499405157592979')
	'''	
	
	
	
	
	
	
	
	
	
	
	
	