from redis import Redis 
from basic import conn

def reflashState(client,count=None,network=None):
	prefix = "client:"
	if not client:
		return False
	x = dict()	
	if count:
		conn().hset(prefix+client,"count",count)
	if network:
		conn().hset(prefix+client,"network",network)
	
	