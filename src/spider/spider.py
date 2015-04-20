#!/usr/bin/env python
# -*- coding:utf-8 -*-
import visiteder
from downer import Downloader
from getlinks import getdoclinks
from urllib import unquote
import re
import sys
sys.path.append("/Users/nantu/projects/racpider/src/")
from coutils import log
class Spider(object):
	def __init__(self, seeds,name):
		self.seeds = seeds # []
		self.visiteder = visiteder.Visited()
		self.name = name
		for x in range(0,len(seeds)):
			self.visiteder.addUnvisitedUrl(seeds[x])
	def fetch(self,url_filter=None):
		while (not self.visiteder.isEmpty() and self.visiteder.getVisitedURLNum()<=1000):
			visited = self.visiteder.unVisitedUrlDequeue()
			if visited is None :
				continue
			if url_filter:
				if url_filter(visited) is None:
					continue
			log.info(unquote(visited),key="FETCH")
			d = Downloader(self.name,visited.split("/")[-1],visited)
			self.visiteder.addVisitedUrl(visited)
			links = getdoclinks(d.get()).parse()
			for x in xrange(0,len(links)):
				self.visiteder.addUnvisitedUrl(links[x])
		log.info("all elements has been fetched",key="INFO")						

if __name__ == "__main__":
	s = Spider(['http://www.jianshu.com/'],"jianshu");
	s.fetch(lambda url:re.compile(r'http://www.jianshu.com/').match(url))