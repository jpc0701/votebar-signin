#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import time
from activation_link import ActEmail

def database_init():
	if os.path.exists('test.db'):
		os.remove('test.db')
	conn = sqlite3.connect('test.db')
	print("Create database successfully")
	'''
	创建表
	'''
	'''
	创建EMAILS表，并初始化数据
	'''
	conn.execute('''CREATE TABLE EMAILS
		   (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
		   USERNAME           TEXT    NOT NULL,
		   PASSWORD           TEXT     NOT NULL);''')
	print("Create Table EMAILS successfully")
	with open('邮箱.txt','r') as f:
		while True:
			email={}
			line = f.readline().replace("\n", "")
			if not line:
				break
			else:
				temp=line.split('----')
				conn.execute("INSERT INTO EMAILS (USERNAME,PASSWORD) VALUES (?,?)",(temp[0],temp[1]))
		print('Date Init successfully')
	conn.commit()
	'''
	创建VOTEBAR表
	'''
	conn.execute('''CREATE TABLE VOTEBAR
		   (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
		   USERNAME           TEXT    NOT NULL,
		   PASSWORD           TEXT     NOT NULL,
		   ACCOUNTID		  TEXT,
		   NAME				  TEXT     NOT NULL,
		   BIRTHDAY			  TEXT,
		   SEX				  TEXT,
		   ADDRESS			  TEXT,
		   ACTIVATION		  BOOLEAN	NOT NULL,
		   QUESTIONNAIRES	  TEXT,
		   POINTS			  INTEGER);''')
	print("Create Table VOTEBAR successfully")	
	'''
	创建PLATFORMS表
	'''
	conn.execute('''CREATE TABLE PLATFORMS
		   (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
		   PLATFORM           TEXT    NOT NULL,
		   COUNTS           INTEGER);''')
	conn.execute("INSERT INTO PLATFORMS (PLATFORM,COUNTS) VALUES (?,?)",('www.votebar.com',0))
	conn.commit()
	print("Create Table PLATFORMS successfully")	
	'''
	创建QUIP表
	'''
	conn.execute('''CREATE TABLE QUIP
		   (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
        QUESTIONNAIRE    TEXT    NOT NULL,
		    IP    TEXT);''')
	conn.commit()
	print("Create Table QUIP successfully")		
	'''
	创建视图
	'''
	conn.execute('''CREATE VIEW VOTEBAR_COUNT AS SELECT COUNT(*) FROM VOTEBAR;''')
	print("Create View VOTEBAR_COUNT successfully")	
	conn.execute('''CREATE VIEW VOTEBAR_NOACCOUNTID AS SELECT * FROM VOTEBAR WHERE ACCOUNTID IS NULL;''')
	print("Create View VOTEBAR_NOACCOUNTID successfully")	
	conn.execute('''CREATE VIEW VOTEBAR_NONACTIVATED AS SELECT * FROM VOTEBAR WHERE ACTIVATION=0;''')
	print("Create View VOTEBAR_NONACTIVATED successfully")	
	conn.execute('''CREATE VIEW [VOTEBAR_NOQUESTIONNAIRE] AS SELECT * FROM VOTEBAR WHERE QUESTIONNAIRES IS NULL;''')
	print("Create View VOTEBAR_NOQUESTIONNAIRE successfully")	
	conn.execute('''CREATE VIEW [VOTEBAR_QUESTIONNAIRE] AS SELECT * FROM VOTEBAR WHERE QUESTIONNAIRES IS NOT NULL;''')
	print("Create View VOTEBAR_QUESTIONNAIRE successfully")	
	conn.execute('''CREATE VIEW VOTEBAR_UNREGISTER_EMAILS AS SELECT * FROM EMAILS WHERE USERNAME NOT IN (SELECT USERNAME FROM VOTEBAR);''')
	print("Create View VOTEBAR_UNREGISTER_EMAILS successfully")	
	conn.commit()
	print('Create Views successfully')
	'''
	创建触发器
	'''
	conn.execute('''CREATE TRIGGER UPDATA_PLATFORMS_INSERT AFTER INSERT ON VOTEBAR BEGIN UPDATE PLATFORMS SET COUNTS=(select * from votebar_count) WHERE ID=1; END;''')
	print('Create Trigger UPDATA_PLATFORMS_INSERT AFTER INSERT ON VOTEBAR successfully')
	conn.execute('''CREATE TRIGGER UPDATA_PLATFORMS_DELETE AFTER DELETE ON VOTEBAR BEGIN UPDATE PLATFORMS SET COUNTS=(select * from votebar_count) WHERE ID=1; END;''')
	print('Create Trigger UPDATA_PLATFORMS_DELETE AFTER DELETE ON VOTEBAR successfully')
	conn.commit()	
	print('Create Trigger successfully')
	conn.close()
		
def Insert(Table_name,fields,values):
	conn = sqlite3.connect('test.db')
	fields=','.join(fields)
	values_p=[]
	for value in values:
		if type(value)==str:
			value='"'+value+'"'
		else:
			value=str(value)
		values_p.append(value)
	values=','.join(values_p)
	SQLstr='INSERT INTO %s (%s) VALUES (%s)'%(Table_name,fields,values)
	conn.execute(SQLstr)
	conn.commit()
	conn.close()

def Update(Table_name,field,value,username):
	conn = sqlite3.connect('test.db')
	username='"'+username+'"'
	if type(value)==str:
		value='"'+value+'"'
	else:
		value=str(value)
	SQLstr="UPDATE %s SET %s = %s WHERE USERNAME=%s"%(Table_name,field,value,username)
	conn.execute(SQLstr)
	conn.commit()
	conn.close()

def Delete(Table_name,field,value):
	conn = sqlite3.connect('test.db')
	if type(value)==str:
		value='"'+value+'"'
	else:
		value=str(value)
	SQLstr='DELETE FROM %s WHERE %s = %s'%(Table_name,field,value)
	conn.execute(SQLstr)
	conn.commit()
	conn.close()	
	
def unregister_emails():
	conn = sqlite3.connect('test.db')
	cursor = conn.execute("SELECT USERNAME,PASSWORD FROM VOTEBAR_UNREGISTER_EMAILS")
	emails=[]
	for i in cursor:
		j={}
		j['email']=i[0]
		j['password']=i[1]
		emails.append(j)
	conn.close()
	return emails
	
def unregister_email():
	conn = sqlite3.connect('test.db')
	cursor = conn.execute("SELECT USERNAME,PASSWORD FROM VOTEBAR_UNREGISTER_EMAILS")
	email={}
	for i in cursor:
		j={}
		email['email']=i[0]
		email['password']=i[1]
		break
	conn.close()
	return email

def get_ip_list(questionnaire):
	conn = sqlite3.connect('test.db')
	SQLstr='SELECT IP FROM QUIP WHERE QUESTIONNAIRE="%s"'%questionnaire
	cursor = conn.execute(SQLstr)
	List=[]
	for ip in cursor:
		List=ip[0].split('|')
		break
	conn.close()
	return List
	
def add_ip(questionnaire,ip):
	ip_list=get_ip_list(questionnaire)
	ip_list.append(ip)
	ip='|'.join(ip_list)
	conn = sqlite3.connect('test.db')
	SQLstr='UPDATE QUIP SET IP = "%s" WHERE QUESTIONNAIRE="%s"'%(ip,questionnaire)
	conn.execute(SQLstr)
	conn.commit()
	conn.close()
	
def update_questionnaire(account,questionnaire):
	conn = sqlite3.connect('test.db')
	SQLstr='UPDATE VOTEBAR SET QUESTIONNAIRES = "%s" WHERE ACCOUNTID="%s"'%(questionnaire,account)
	conn.execute(SQLstr)
	conn.commit()
	conn.close()

def get_account():
	conn = sqlite3.connect('test.db')
	cursor = conn.execute('SELECT ACCOUNTID FROM VOTEBAR_NOQUESTIONNAIRE WHERE ACCOUNTID NOT NULL')
	account=''
	for i in cursor:
		account=i[0]
		break
	conn.close()
	return account
	
def add_emails(filename):
	conn = sqlite3.connect('test.db')
	with open(filename,'r') as f:
		while True:
			email={}
			line = f.readline().replace("\n", "")
			if not line:
				break
			else:
				temp=line.split('----')
				conn.execute("INSERT INTO EMAILS (USERNAME,PASSWORD) VALUES (?,?)",(temp[0],temp[1]))
		print('Date Init successfully')
	conn.commit()	
	conn.close()

def get_noaccount():
	conn = sqlite3.connect('test.db')
	cursor = conn.execute('SELECT USERNAME,PASSWORD FROM VOTEBAR_NOACCOUNTID')
	l={}
	for i in cursor:
		l['username']=i[0]
		l['password']=i[1]
		break
	conn.close()
	return l
	
	
	
if __name__ == '__main__':
	#print(get_noaccount())
	database_init()

























