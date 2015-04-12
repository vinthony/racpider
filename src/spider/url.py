#!/usr/bin/env python
# -*- coding:utf-8 -*-
#处理url
class Url(object):
	"""docstring for Url"""
	def __init__(self,path):
		self.path = path

	def _parsepath():
		#cond1: [www,bbs,tieba].baidu.com
		#cond2: bbs.tieba.com/[20140402-20120202].html
		#cond3: bbs.tieba.com/page=[1-10000]
		#cond4: https问题？post问题？			