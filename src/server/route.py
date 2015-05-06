from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redisQueue import RedisQueue
from bloomfilter import BloomFilter
from redis import Redis
import sys,os
from config.getconfig import getconfig
from utils import log
from urllib import unquote
import time
import re
config = getconfig()
bf = BloomFilter()
rc = re.compile(config['regexp'])
rec = config['redis']
redis_conn = Redis(host=rec["host"],port=int(rec["port"]),db=int(rec['db']))
rq = RedisQueue(config['name'],redis_conn)


def legal(url):
	return rc.search(url)

@get('/')
def index():
	return 'racpider'

@get('/pull')
def pull():
	if not rq.empty():
		u = rq.dequeue()
		bf.add(u)
		log.info(unquote(u),key="FETCH")
		return u
	else:
		return seeother("/error")	

@get('/error')
def error():
	return "error occur"
	
@get('/push')
def push():
	urls = ctx.request.header('file').split(",")
	for x in urls:
		if legal(x):
			if not bf.contains(x):
				rq.enqueue(x)
				bf.add(x)
			else:
				pass
				# print "in bf"
		else:
			pass
			# print "inlegal"			

	
@get('/empty')
def empty():
	return str(rq.qsize())