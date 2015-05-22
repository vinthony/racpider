from redis import Redis
from config.getconfig import getconfig

def conn():
	config = config()
	rec = getconfig()["redis"]
	self.conn =  Redis(host=rec["host"],port=int(rec["port"]),db=int(rec['db']))
	return self.conn