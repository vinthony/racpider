from redis import Redis 
from config.getconfig import getconfig

class rclient(object):
	def __init__(self):
		rec = getconfig()["redis"]
		self.conn =  Redis(host=rec["host"],port=int(rec["port"]),db=int(rec['db']))
	def set(self,key,value):
		self.conn.set(key,value)
	def get(self,key):
		return self.conn.get(key)	