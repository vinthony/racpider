#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,functools,

# from utils import log
def _reg_exp(path):
	pass;

def fetch(path):
	def _decorator(func):
		@functools.wraps(func)
		def _wrapper(*args,**kw):
			headers = requests.get(path).headers
			body = requests.get(path).text.encode('UTF-8')
			return func(headers,body,*args,**kw)
		return _wrapper
	return _decorator		

if __name__ == "__main__":

	@fetch("http://www.baidu.com")
	def test(headers,body):
		print headers
		print body

	test()	