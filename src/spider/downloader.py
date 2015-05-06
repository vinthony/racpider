#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests
import io,sys,os
import time
from urllib import unquote
from status import NetworkStatus
from utils import log

class Downloader(object):
	def __init__(self,dir,name,url):
		self.url = url
		self.name = name
		self.dir = dir
	def get(self):
		r = requests.get(self.url)
		if r.status_code != NetworkStatus.OK:
			log.warning("error:"+str(r.status_code)+":"+str(self.url))
		log.info(self.url,key="FETCH")
		if self.save(self.name,r.text):
			return r.text
		else:
			return "404"	

	def save(self,name,body):
		if body is None:
			return
		p = os.path.dirname(os.path.join(os.path.abspath("."),os.pardir))+"/data/"+self.dir+"/"
	 	try:
			os.isdir(p)
		except Exception,e:
			p = os.path.dirname(os.path.join(os.path.abspath("."),os.pardir))+"/data/"+self.dir+"/"
		if not os.path.exists(p):
			os.makedirs(p)
		if not name or len(name) > 100:
			name = unquote(self.dir+str(time.time()))
		try:
			name = unquote(name).decode("utf-8")
			
		except Exception,e:
			name = unquote(self.dir+str(time.time()))
			
		with io.open(p+"/"+name+".rac",'w') as file:
				file.write(body)
		return True		

if __name__ == '__main__':
	d = Downloader("test2","http://www.baidu.com")
	d.get()		
