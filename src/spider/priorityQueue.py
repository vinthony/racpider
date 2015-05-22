from spider.models import URL
from urlparse import urlparse
from dns.lookupandsave import geturldict
from heapq import heappush,heappop
from utils import log
class priorityQueue(object):
	def __init__(self):
		self.q = []

	def addtoQueue(self,obj):
		heappush(self.q,URL(search=obj['search'],ip=obj['ip'],host=obj['host'],priority=obj['priority'],depth=obj['depth'],port=obj['port']))

	def deQueueURL(self):
		obj = heappop(self.q)
		return "http://"+obj['host']+obj['search']
	def addURLtoQueue(self,url):
		self.addtoQueue(geturldict(url))
	def count(self):
		return len(self.q)