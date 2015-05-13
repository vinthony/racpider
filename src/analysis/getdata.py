#!/usr/bin/env python
from script import Items
from config.getconfig import getconfig
from pymongo import MongoClient

config = getconfig()
parser = Items()
for item in config.clients:
	client = MongoClient(item['host'],item['port'])
	db = client['racpider']
	collection = client[parser.name]
	if len(collection) == 0:
		continue
	for m in collection:
		if parser.filter():
			parser.parse(m.body)
