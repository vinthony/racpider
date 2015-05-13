from pymongo import MongoClient
from config.getconfig import getconfig

class MongoC(object):
	def __init__(self):
		cf = getconfig()
		mc = cf['mongodb']
		self.client =  MongoClient(mc['host'],int(mc['port']))
		self.db  = self.client[mc['name']]
		self.collection = self.db[cf['name']]

	def insert(self,obj):
		if self.collection.find({"url":obj.format()["url"]}).count() == 0:
			self.collection.insert_one(obj.format())	
