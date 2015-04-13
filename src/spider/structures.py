#!/usr/bin/env python

"""
Queue:
	saving the list of fetching
"""

class Queue(object):
	queue = [];
	def __init__(self):
		pass
	def enqueue(self,item):
		self.queue.append(item)
	def dequeue(self):
		temp = self.queue[0]
		del self.queue[0]
		return temp	
	def isEmpty(self):
		return len(self.queue) == 0
	def isContain(self,t):
		for x in range(0,len(self.queue)):
			if self.queue[x] == t:
				return True
		return False		
	def __repr__(self):
		return str(self.queue)
if __name__ == '__main__':
	q = Queue()
	q.enqueue("111")
	q.enqueue("222")
	q.dequeue()
	print q.isEmpty()
	print q.isContain("111")	
	print q.isContain("222")
