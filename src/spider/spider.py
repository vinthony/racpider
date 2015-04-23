#!/usr/bin/env python
# -*- coding:utf-8 -*-
import visiteder
from downloader import Downloader
from getlinks import getdoclinks
from urllib import unquote
import re
import sys
import time
sys.path.append("/Users/nantu/projects/racpider/src/")
from utils import log
from config import getconfig
			
class Spider(object):
	def __init__(self, seeds,name,re_filter=None):
		self.seeds = seeds # []
		self.visiteder = visiteder.Visited()
		self.filter = re_filter
		self.name = name
		self.config = getconfig.getconfig()
		self.stop = self.config["stop"]
		self.tc_function = self.timeCondition_iter()
		for x in range(0,len(seeds)):
			self.visiteder.addUnvisitedUrl(seeds[x])

	def pageCondition(self):
		num = self.visiteder.getVisitedURLNum()
		config = self.stop
		if int(config["pages"]) > num :
			return True
		else:
			return False
		
	def timeCondition_iter(self):
		config = self.stop
		t = time.time()
		def time_iter(now):
			if now - t < float(config["time"]) :
				return True
			else:
				return False
		return time_iter			
	
	def timeCondition(self):
		return self.tc_function(time.time())

	def loopCondition(self):
		config = self.stop
		if int(config["pages"]) != 0:
			return self.pageCondition() and self.notEmpty()
		if int(config["time"]) != 0 :
			return self.timeCondition() and self.notEmpty()

	def notEmpty(self):
		return not self.visiteder.isEmpty()# 未访问的队列不为空
	def fetch_iter(self):
		visited = self.visiteder.unVisitedUrlDequeue()
		if visited is None :
			continue
		if url_filter:
			if url_filter(visited) is None:
				continue
		else:
			if rc.search(visited) is None:
				continue	
		d = Downloader(self.name,visited.split("/")[-1],visited)
		self.visiteder.addVisitedUrl(visited)
		links = getdoclinks(d.get()).parse()
		for x in xrange(0,len(links)):
			self.visiteder.addUnvisitedUrl(links[x])

	def fetch(self,url_filter=None):
		rc = re.compile(self.filter)
		log.displayConfig()
		while(self.loopCondition())
			fetch_iter()
		log.info("all elements has been fetched",key="INFO")						

if __name__ == "__main__":
	s = Spider(['http://www.ifanr.com/'],"ifanr",r"http://www.ifanr.com");
	s.fetch()