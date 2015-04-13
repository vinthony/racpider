#!/usr/bin/env python
# -*- coding: utf-8 -*-
import visiteder

class Spider(object):
	def __init__(self, seeds):
		self.seeds = seeds # []
		self.visiteder = visiteder.Visited()
		for x in range(0,len(seeds)):
			self.visiteder.addUnvisitedUrl(seeds[x])
	def fetch(self,url_filter):
		pass;

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

	@fetch("www.baidu.com")
	def test(body):
		pass
		#print body

	test()	