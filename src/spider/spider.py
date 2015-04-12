#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,functools
from lxml import etree
import io,sys
# from utils import log
def downloader(func_name,body):
	with io.open(func_name+".rac",'w') as file:
		file.write(body)

def getFuncName(func):
	return str(func).split(" ")[1]
def stardard_url(path):
	if path.startswith("http://") or path.startswith("https://"):
		print path
		return path
	else:
		return "http://"+path
		
def fetch(path):
	def _decorator(func):
		@functools.wraps(func)
		def _wrapper(*args,**kw):
			#错误处理
			#download the page
			r = requests.get(stardard_url(path));
			headers = r.headers
			if r.status_code > 400:
				raise Exception("network connection failed") 
			body = r.text
			downloader(getFuncName(func),body)
			return func(body,*args,**kw)
		return _wrapper
	return _decorator		

if __name__ == "__main__":

	#fetch('get',http://[u+].baidu.com)
	@fetch("www.baidu.com")
	def test(body):
		pass
		#print body

	test()	