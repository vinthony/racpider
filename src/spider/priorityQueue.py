from spider.models import URL
from urlparse import urlparse
from dns.lookupandsave import geturldict
from heapq import heappush,heappop
from utils import log
class priorityQueue(object):
	def __init__(self):
		self.q = []

	def addtoQueue(self,obj):
		print obj['depth']
		heappush(self.q,URL(obj))

	def deQueueURL(self):
		obj = heappop(self.q)
		log.info(obj)
		return obj
	def addURLtoQueue(self,url):
		self.addtoQueue(URL(geturldict(url)))
	def count(self):
		return len(self.q)