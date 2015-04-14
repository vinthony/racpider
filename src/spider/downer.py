#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import io,sys
from status import NetworkStatus
class Downloader(object):
	def __init__(self,name,url):
		self.url = url
		self.name = name
	def get(self):
		r = requests.get(self.url)
		if r.status_code != NetworkStatus.OK:
			raise Exception("network connection failed") 
		self.save(self.name,r.text)	
		return r.text

	def save(self,name,body):
		with io.open(name+".rac",'w') as file:
			file.write(body)

if __name__ == '__main__':
	d = Downloader("test2","http://www.baidu.com")
	d.get()		