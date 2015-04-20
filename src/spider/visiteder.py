#!/etc/bin/env python
import structures
"""
a list of Visited url
"""

class Visited(object):
	visited = set()
	urls = structures.Queue()
	def __init__(self):
		pass
		
	def getUnvisitedUrl(self):
		return self.urls
	
	def addVisitedUrl(self,url):
		return self.visited.add(url)
	
	def removeVisitedUrl(self,url):
		self.visited.remove(url)		
	
	def unVisitedUrlDequeue(self):
		return self.urls.dequeue()
	
	def addUnvisitedUrl(self,url):
		if url and url.strip() and url not in self.visited and not self.urls.isContain(url):
			self.urls.enqueue(url)

	def getVisitedURLNum(self):
		return len(self.visited)

	def isEmpty(self):
		return self.urls.isEmpty()

if __name__ == "__main__":
	visit = Visited()
	visit.addUnvisitedUrl("111");
	visit.addUnvisitedUrl("222");
	print visit.urls
	visit.addVisitedUrl(visit.unVisitedUrlDequeue())
	print visit.getVisitedURLNum()
	print visit.isEmpty()
