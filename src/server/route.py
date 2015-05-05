from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redisQueue import RedisQueue
from bloomfilter import BloomFilter
import sys,os
sys.path.append("/Users/nantu/projects/racpider/src")
from spider.geturlsfromlink import getlinks
import time
import re

bf = BloomFilter()
rc = re.compile("http://jandan.net")
rq = RedisQueue("rac",host="localhost",port=6379,db=0)


def legal(url):
	return rc.match(url)

@get('/')
def index():
	return 'racpider'

@get('/pull')
def pull():
	#rq = RedisQueue("rac",host="localhost",port=6379,db=0)
	if not rq.empty():
		u = rq.dequeue()
		bf.add(u)
		return u
	else:
		return seeother("/error")	

@get('/error')
def error():
	return "error occur"
	
@get('/push')
def push():
	#rq = RedisQueue("rac",host="localhost",port=6379,db=0)
	urls = ctx.request.header('file').split(",")
	for x in urls:
		if legal(x):
			if not bf.contains(x):
				rq.enqueue(x)
				bf.add(x)
			else:
				print "chong fu"	
	
@get('/empty')
def empty():
	#rq = RedisQueue("rac",host="localhost",port=6379,db=0)
	return str(rq.qsize())