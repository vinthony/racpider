from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redisQueue import RedisQueue
import sys
sys.path.append("/Users/nantu/projects/racpider/src")
from spider.geturlsfromlink import getlinks
import time

@get('/')
def index():
	return 'hello,world'

@get('/pull')
def pull():
	r = RedisQueue("rac",host="localhost",port=6379,db=0)
	if not r.empty():
		return r.dequeue()
	else:
		return seeother("404.html")	

@post('/push')
def push():
	urls = ctx.request.header('file').split(",")
	r = RedisQueue("rac",host="localhost",port=6379,db=0)
	# # cookie=urls???
	for x in urls:
		r.enqueue(x)
	
@get('/empty')
def emp():
	r = RedisQueue("rac",host="localhost",port=6379,db=0)
	return r.qsize()