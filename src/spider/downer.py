#!/usr/bin/env python
import io,sys
import requests
import code
class Downloader(object):
	def __init__(self,name,url):
		self.url = url
		self.name = name
	def get(self):
		r = requests.get(url)
		if r.state_code != code.OK:
			raise Exception("network connection failed") 
		self.save(self.name,r.text)	

	def save(name,body):
		with io.open(func_name+".rac",'w') as file:
			file.write(body)

if __name__ == '__init__':
	d = Downloader("v","http://www.baidu.com")
	d.get()		