#!/usr/bin/env python
from script import Items
from config.getconfig import getconfig
from pymongo import MongoClient

config = getconfig()
parser = Items()
def getdata():
	for item in config['clients']:
		client = MongoClient(item['host'],int(item['port']))
		db = client['racpider']
		collection = db[parser.name].find()
		if not collection:
			continue
		for m in collection:
			if parser.filter(m['url']):
				parser.parse(m['body'])
