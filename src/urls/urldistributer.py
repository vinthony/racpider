import json
from server.redisQueue import RedisQueue
from dns.lookupandsave import dristributer
def urldistributer(str_json):
	#  from : address:port
	#  clientstate: (integer) num
	#  urls:[] array
	redis_conn = Redis(host=rec["host"],port=int(rec["port"]),db=int(rec['db']))
	rq = RedisQueue(config['name'],redis_conn)
	while not rq.empty():
		dristributer(rq.dequeue())
	
