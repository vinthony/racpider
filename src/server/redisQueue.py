import uuid
#http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html
class RedisQueue(object):
	def __init__(self,name,redis_conn):
		self.db = redis_conn
		self.key = '%s:%s:' % (name,"queue")

	def qsize(self):
		return self.db.llen(self.key)

	def empty(self):
		return	self.qsize() == 0

	def enqueue(self,item):
		self.db.rpush(self.key,item)

	def dequeue(self,block=True,timeout=None):
		if block:
			item = self.db.blpop(self.key,timeout=timeout)
		else:
			item = self.db.lpop(self.key)
		if item:
			item = item[1]

		return item 		

	def get_nowait(self):
		return self.dequeue(False)
