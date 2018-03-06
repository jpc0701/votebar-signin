#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice,randint
from datetime import datetime
import porxy

surname=['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨', \
		 '朱','秦','尤','许','何','吕','施','张','孔','曹','严','华','金','魏','陶','姜', \
		 '戚','谢','邹','喻','柏','水','窦','章','云','苏','潘','葛','奚','范','彭','郎', \
		 '鲁','韦','昌','马','苗','凤','花','方','俞','任','袁','柳','酆','鲍','史','唐', \
		 '费','廉','岑','薛','雷','贺','倪','汤','滕','殷','罗','毕','郝','邬','安','常', \
		 '乐','于','时','傅','皮','卞','齐','康','伍','余','元','卜','顾','孟','平','黄', \
		 '和','穆','萧','尹','姚','邵','湛','汪','祁','毛','禹','狄','米','贝','明','臧', \
		 '计','伏','成','戴','谈','宋','茅','庞','熊','纪','舒','屈','项','祝','董','梁', \
		 '杜','阮','蓝','闵','席','季','麻','强','贾','路','娄','危','江','童','颜','郭', \
		 '梅','盛','林','刁','锺','徐','邱','骆','高','夏','蔡','田','樊','胡','凌','霍', \
		 '虞','万','支','柯','昝','管','卢','莫','经','房','裘','缪','干','解','应','宗', \
		 '丁','宣','贲','邓','郁','单','杭','洪','包','诸','左','石','崔','吉','钮','龚', \
		 '程','嵇','邢','滑','裴','陆','荣','翁','荀','羊','於','惠','甄','麴','家','封', \
		 '芮','羿','储','靳','汲','邴','糜','松','井','段','富','巫','乌','焦','巴','弓', \
		 '牧','隗','山','谷','车','侯','宓','蓬','全','郗','班','仰','秋','仲','伊','宫', \
		 '宁','仇','栾','暴','甘','钭','历','戎','祖','武','符','刘','景','詹','束','龙', \
		 '叶','幸','司','韶','郜','黎','蓟','溥','宿','白','怀','蒲','邰','从','鄂','索', \
		 '咸','籍','赖','卓','蔺','屠','蒙','池','乔','阳','郁','胥','能','苍','双','闻', \
		 '莘','党','翟','谭','贡','劳','逄','姬','申','扶','堵','冉','宰','郦','雍','却', \
		 '璩','桑','桂','濮','牛','寿','通','边','扈','燕','冀','僪','浦','尚','农','温', \
		 '别','庄','晏','柴','瞿','阎','充','慕','连','茹','习','宦','艾','鱼','容','向', \
		 '古','易','慎','戈','廖','庾','终','暨','居','衡','步','都','耿','满','弘','匡', \
		 '国','文','寇','广','禄','阙','东','欧','殳','沃','利','蔚','越','夔','隆','师', \
		 '巩','厍','聂','晁','勾','敖','融','冷','訾','辛','阚','那','简','饶','空','曾', \
		 '毋','沙','乜','养','鞠','须','丰','巢','关','蒯','相','查','后','荆','红','游']
		 
givenname_f=['梦琪','之雅','之桃','慕青','尔岚','初夏','沛菡','傲珊','曼文','乐菱','惜文', \
			 '香寒','新柔','语蓉','夜蓉','涵柏','水桃','醉蓝','语琴','从彤','傲晴','语兰', \
			 '又菱','碧彤','元霜','怜梦','紫寒','妙彤','曼易','南莲','紫翠','雨寒','易烟', \
			 '如萱','若南','寻真','晓亦','向珊','慕灵','以蕊','映易','雪柳','海云','凝天', \
			 '沛珊','寒云','冰旋','宛儿','绿真','晓霜','碧凡','夏菡','曼香','若烟','半梦', \
			 '雅绿','冰蓝','灵槐','平安','书翠','翠风','代云','梦曼','幼翠','听寒','梦柏', \
			 '醉易','访旋','亦玉','凌萱','访卉','怀亦','笑蓝','靖柏','夜蕾','冰夏','梦松', \
			 '书雪','乐枫','念薇','靖雁','从寒','觅波','静曼','凡旋','以亦','念露','芷蕾', \
			 '千兰','新波','代真','新蕾','雁玉','冷卉','紫山','千琴','傲芙','盼山','怀蝶', \
			 '冰兰','山柏','翠萱','问旋','白易','问筠','如霜','半芹','丹珍','冰彤','亦寒', \
			 '之瑶','冰露','尔珍','谷雪','乐萱','涵菡','海莲','傲蕾','青槐','易梦','惜雪']		 
		 
givenname_m=['博文','梓晨','胤祥','瑞霖','明哲','天翊','凯瑞','健雄','耀杰','潇然','子涵', \
			 '越彬','钰轩','智辉','致远','俊驰','雨泽','烨磊','晟睿','文昊','修洁','黎昕', \
			 '远航','旭尧','鸿涛','伟祺','荣轩','越泽','浩宇','瑾瑜','皓轩','擎苍','擎宇', \
			 '志泽','子轩','睿渊','弘文','哲瀚','雨泽','楷瑞','建辉','晋鹏','天磊','绍辉', \
			 '泽洋','鑫磊','鹏煊','昊强','伟宸','博超','君浩','子骞','鹏涛','炎彬','鹤轩', \
			 '越彬','风华','靖琪','明辉','伟诚','明轩','健柏','修杰','志泽','弘文','峻熙', \
			 '嘉懿','煜城','懿轩','烨伟','苑博','伟泽','熠彤','鸿煊','博涛','烨霖','烨华', \
			 '煜祺','智宸','正豪','昊然','明杰','立诚','立轩','立辉','峻熙','弘文','熠彤', \
			 '鸿煊','烨霖','哲瀚','鑫鹏','昊天','思聪','展鹏','笑愚','志强','炫明','雪松', \
			 '思源','智渊','思淼','晓啸','天宇','浩然','文轩','鹭洋','振家','乐驹','晓博', \
			 '文博','昊焱','立果','金鑫','锦程','嘉熙','鹏飞','子默','思远','浩轩','语堂']		 

address_province=['江苏','山东','广东','浙江','福建','北京','上海']
address_city={'江苏':['徐州','宿迁','连云港','淮安','盐城','扬州','泰州','南通','镇江','常州','无锡','苏州','南京'], \
			  '山东':['济南','泰安','潍坊','德州','滨州','莱芜','青岛','烟台','日照','东营','济宁','菏泽','聊城','临沂','枣庄','淄博','威海'], \
			  '广东':['珠海','东莞','佛山','中山','惠州','汕头','江门','茂名','肇庆','湛江','梅州','汕尾','河源','清远','韶关','揭阳','阳江','潮州','云浮'], \
			  '浙江':['杭州','宁波','温州','嘉兴','湖州','绍兴','金华','衢州','舟山','台州','丽水'], \
			  '福建':['泉州','三明','南平','龙岩','漳州','宁德','莆田','福州','厦门'], \
			  '河南':['郑州','新乡','洛阳','安阳','焦作','许昌','平顶山','漯河','开封','濮阳','鹤壁','南阳','三门峡','驻马店','商丘','信阳','周口'], \
			  '北京':['北京市'], \
			  '上海':['上海市']}
			 
sex=['男','女']			
		 
class Person(object):
	def __init__(self,surname='0',givenname='0',birthday='0',sex='0',address='0'):
		self.__surname=surname
		self.__givenname=givenname
		self.__birthday=birthday
		self.__sex=sex
		self.__address=address
		self.__info={}
		self.generate_info()
	
	def generate_info(self):
		if self.__surname == '0':
			self.__surname=choice(surname)
			self.__info['surname']=self.__surname
		if self.__birthday == '0':
			randtime=datetime.fromtimestamp(randint(315504000,946656000))
			self.__birthday=randtime.strftime('%Y-%m-%d')
			self.__info['birthday_y']=randtime.strftime('%Y')
			self.__info['birthday_m']=randtime.strftime('%m')
			self.__info['birthday_d']=randtime.strftime('%d')
			self.__info['birthday']=self.__birthday
		if self.__sex == '0':
			self.__sex=choice(sex)
			self.__info['sex']=self.__sex
		if self.__givenname == '0':
			if self.__sex=='男':
				self.__givenname=choice(givenname_m)
			elif self.__sex=='女':
				self.__givenname=choice(givenname_f)
			self.__info['givenname']=self.__givenname
			self.__info['name']=self.__surname+self.__givenname
		if self.__address=='0':
			self.__info['address_province']=choice(address_province)
			self.__info['address_city']=choice(address_city[self.__info['address_province']])
			self.__info['address']=self.__info['address_province']+' '+self.__info['address_city']
	
	def info(self):
		return self.__info
			
	def info_str(self):
		return '%s%s %s %s %s'%(self.__info['surname'],self.__info['givenname'],self.__info['sex'],self.__info['birthday'],self.__info['address'])
		
if __name__ == '__main__':
#	for i in range(100):
#		per=Person()
#		print(per.info_str())
	for pro in 	address_province:
		for city in address_city[pro]:
			print(city,end='')
			print(porxy.Proxy_IP(city))
		 
		 
		 
		 
		 
		 
		 
		 
		 