from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redisQueue import RedisQueue
import sys
sys.path.append("/Users/nantu/projects/racpider/src")
from spider.geturlsfromlink import getlinks
import time

@get('/')
def index():
	return 'hello,world'

## uuid pull的时候使用uuid来确保没有缓存
@get('/pull')
def pull():
	r = RedisQueue("rac",host="localhost",port=6379,db=0)
	if not r.empty():
		return r.dequeue()
	else:
		return seeother("404.html")	

@get('/push/:time')
def push(time):
	urls = ctx.request.cookie("urls").split(',')
	r = RedisQueue("rac",host="localhost",port=6379,db=0)
	# cookie=urls???
	for x in urls:
		r.enqueue(x)
	
