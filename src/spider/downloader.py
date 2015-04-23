#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import io,sys,os
import time
from urllib import unquote
from status import NetworkStatus
sys.path.append("/Users/nantu/projects/racpider/src/")
from utils import log
class Downloader(object):
	def __init__(self,dir,name,url):
		self.url = url
		self.name = name
		self.dir = dir
	def get(self):
		log.info(unquote(self.url),key="FETCH")
		r = requests.get(self.url)
		if r.status_code != NetworkStatus.OK:
			log.warning("error:"+str(r.status_code)+":"+str(self.url))
			# raise Exception("network connection failed")
		self.save(self.name,r.text)	
		return r.text

	def save(self,name,body):
		if body is None:
			return
		p = "/Users/nantu/projects/racpider/data/"+self.dir+"/"
		if not os.path.exists(p):
			os.makedirs(p)
		if not name:
			name = unquote(self.dir+str(time.time()))	
		with io.open(p+"/"+unquote(name)+".rac",'w') as file:
			file.write(body)

if __name__ == '__main__':
	d = Downloader("test2","http://www.baidu.com")
	d.get()		