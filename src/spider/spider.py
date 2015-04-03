#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,functools
# from utils import log
def _reg_exp(path):
	pass;

def fetch(path):
	def _decorator(func):
		@functools.wraps(func)
		def _wrapper(*args,**kw):
			print requests.get(path).text.encode()
			return func(*args,**kw)
		return _wrapper
	return _decorator		

if __name__ == "__main__":

	@fetch("http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/")
	def test():
		return 1
	test()	