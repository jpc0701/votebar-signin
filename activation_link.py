#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

class Link_HTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.__link=''

	def get_link(self):
		return self.__link
		
	def handle_starttag(self, tag, attrs):
		if tag=='a':
			for name,value in attrs:
				if name=='href':
					if value.startswith('http://www.votebar.com/user/EmailSuccessful.aspx?'):
						self.__link=value

class ActEmail(object):
	def __init__(self,username,password,pop3_server):
		self.__email = username
		self.__password = password
		self.__pop3_server = pop3_server
		self.__isConnect=False
		try_times=0
		while True:
			try_times+=1
			try:
#				print('正在第%d次尝试连接......'%try_times)
				self.__server = poplib.POP3(self.__pop3_server)
#				self.__server.set_debuglevel(1)
#				print(self.__server.getwelcome().decode('utf-8'))
				self.__server.user(self.__email)
				self.__server.pass_(self.__password)
#				print('连接成功---->Messages: %s. Size: %s' % self.__server.stat())
				self.__isConnect=True
				break
			except:
#				print('第%d次尝试连接失败'%try_times)
				if try_times>=5:
					self.__isConnect=False
					break

	def get_activation_link(self):
		if self.__isConnect==True:
			try:
				resp, mails, octets = self.__server.list()
				index = len(mails)
				for i in range(1,index+1):
					resp, lines, octets = self.__server.retr(i)
					try:
						msg_content = b'\r\n'.join(lines).decode('utf-8')
					except:
						msg_content = b'\r\n'.join(lines).decode('gbk')
					msg = Parser().parsestr(msg_content)
					if self.get_Subject(msg)=='请完成投吧网E-mail激活':
						self.__server.quit()
						link=Link_HTMLParser()
						link.feed(self.get_Html(msg))
						return link.get_link()
			except:
				return '无法解析邮件！'
		else:
			return '无法连接到邮箱！'
		
	def get_Subject(self,msg):
		Subject='无'
		if msg.get('Subject', '')!=None:
			Subject= self.decode_str(msg.get('Subject', '')).strip()
		return Subject
		
	# indent用于缩进显示:
	def get_Html(self,msg, indent=0):
		if msg.is_multipart():
			parts = msg.get_payload()
			for n, part in enumerate(parts):
				return self.get_Html(part, indent + 1)
		else:
			content_type = msg.get_content_maintype()
			if content_type=='text':
#				return msg.get_content_charset()
				with open('1.txt','w') as f:
					f.write(msg.get_payload(decode=True).decode('utf-8'))
#				print(msg.get_payload(decode=True).decode('utf-8'))
				return msg.get_payload(decode=True).decode('utf-8')

	def guess_charset(self,msg):
		charset = msg.get_charset()
		if charset is None:
			content_type = msg.get('Content-Type', '').lower()
			pos = content_type.find('charset=')
			if pos >= 0:
				charset = content_type[pos + 8:].strip()
		return charset

	def decode_str(self,s):
			value, charset = decode_header(s)[0]
			if charset:
				value = value.decode(charset)
			return value	


if __name__ == '__main__':
	Activation=ActEmail('jishi274824497@sohu.com','biba8143398','smtp.sohu.com')
	print(Activation.get_activation_link())
		
		
		
		
		
		