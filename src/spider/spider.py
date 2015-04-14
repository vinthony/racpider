#!/usr/bin/env python
# -*- coding:utf-8 -*-
import visiteder
from downer import Downloader
from getlinks import getdoclinks
import re
import sys
sys.path.append("..")
from coutils import log
class Spider(object):
	def __init__(self, seeds):
		self.seeds = seeds # []
		self.visiteder = visiteder.Visited()
		for x in range(0,len(seeds)):
			self.visiteder.addUnvisitedUrl(seeds[x])
	def fetch(self,url_filter=None):
		while (not self.visiteder.isEmpty() and self.visiteder.getVisitedURLNum()<=1000):
			visited = self.visiteder.unVisitedUrlDequeue()
			if visited is None or type(visited) != type("str"):
				continue
			if url_filter:
				if url_filter(visited) is None:
					continue
			log.info('exe '+visited)
			d = Downloader(visited.split("/")[-1],visited)
			b = d.get()
			self.visiteder.addVisitedUrl(visited)
			gdl = getdoclinks(b)
			links = gdl.parse()
			for x in xrange(0,len(links)):
				self.visiteder.addUnvisitedUrl(links[x])				

if __name__ == "__main__":
	s = Spider(["http://jandan.net/"]);
	s.fetch()