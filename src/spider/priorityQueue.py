from spider.models import URL
from urlparse import urlparse
from dns.lookupandsave import geturldict
from heapq import heappush,heappop
from utils import log
from server.bloomfilter import BloomFilter
from config.getconfig import getconfig
import re


class priorityQueue(object):
	def __init__(self):
		self.q = []
		self.bf = BloomFilter()
		config = getconfig()
		self.rc = re.compile(config['regexp'])

	def inlegal(self,url):
		return not self.rc.search(url)	

	def addtoQueue(self,obj):
		if self.bf.contains(self.geturlfromobj(obj)) or self.inlegal(self.geturlfromobj(obj)):
			pass
		else:
			heappush(self.q,URL(search=obj['search'],ip=obj['ip'],host=obj['host'],priority=obj['priority'],depth=obj['depth'],port=obj['port']))
			self.bf.add(self.geturlfromobj(obj))

	def geturlfromobj(self,obj):
		return "http://"+obj['host']+obj['search']
	def deQueueURL(self):
		obj = heappop(self.q)
		return self.geturlfromobj(obj)
	def addURLtoQueue(self,url):
		self.addtoQueue(geturldict(url))
	def count(self):
		return len(self.q)