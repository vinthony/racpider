#!/usr/bin/env python 
# -*- coding:utf8 -*-
import os
from server import route
from redis import Redis
from server.web import WSGIApplication
from server.redisQueue import RedisQueue
from config.getconfig import getconfig
from dns.lookupandsave import geturldict
# - config the redis
config = getconfig()
rc = config["redis"]
redis_conn = Redis(host=rc["host"],port=int(rc["port"]),db=int(rc['db']))

r = RedisQueue(config["name"],redis_conn)

if r.empty():
	for x in config["seeds"]:
		r.enqueue(geturldict(x))

wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
wsgi.add_module(route)
wsgi.run(config["server"])

