# coding:utf-8
from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redisQueue import RedisQueue
from bloomfilter import BloomFilter
from redis import Redis
import sys,os,json
from config.getconfig import getconfig
from utils import log
from urllib import unquote
from redistool.clientinfo import reflashState
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
	## pull 通过header得知状态，然后分配
	if not rq.empty():
		u = rq.dequeue()
		us = "http://"+u['host']+u['search']
		bf.add(u)
		log.info(unquote(us),key="FETCH")
		return u
	else:
		return seeother("/error")	

@get('/error')
def error():
	return "error occur"
	
@get('/push')
def push():
	urls = json.loads(ctx.request.header('file'))
	for x in urls:
		if legal(x):
			if not bf.contains(x):
				rq.enqueue(geturldict(x))
				bf.add(x)
	return "1-ok"
	
@get('/empty')
def empty():
	client = ctx.request.header('clinet')
	count = ctx.request.header('count')
	network = ctx.request.header('network')
	reflashState(client,count=count,network=network)
	return str(rq.qsize())