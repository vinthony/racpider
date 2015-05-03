from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redisQueue import RedisQueue
from bloomfilter import BloomFilter

import sys
sys.path.append("/Users/nantu/projects/racpider/src")
from spider.geturlsfromlink import getlinks
import time
import re

bf = BloomFilter()
rq = RedisQueue("rac",host="localhost",port=6379,db=0)
rc = re.compile("http://jandan.net")

def legal(url):
	return rc.match(url)
@get('/')
def index():
	return 'racpider'

@get('/pull')
def pull():
	rq = RedisQueue("rac",host="localhost",port=6379,db=0)
	if not rq.empty():
		u = rq.dequeue()
		bf.add(u)
		return u
	else:
		return seeother("404.html")	

@get('/push')
def push():
	rq = RedisQueue("rac",host="localhost",port=6379,db=0)
	urls = ctx.request.header('file').split(",")
	for x in urls:
		if not bf.contains(x) and legal(x):
			rq.enqueue(x)
	
@get('/empty')
def empty():
	rq = RedisQueue("rac",host="localhost",port=6379,db=0)
	print rq.dequeue()
	return str(rq.qsize())