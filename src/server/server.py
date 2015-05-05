#!/usr/bin/env python 
# -*- coding:utf8 -*-
from web import WSGIApplication
import os
import route

from redisQueue import RedisQueue
# - config the redis

r = RedisQueue("rac",host="localhost",port=6379,db=0)

if r.empty():
	r.enqueue("http://www.jandan.net")
	
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
wsgi.add_module(route)
wsgi.run(5237, host='0.0.0.0')
# web(os.path.dirname(os.path.abspath(__file__))).run("127.0.0.1",5237)

