from web import get,post,ctx,interceptor,seeother,notfound,found,Dict
from redis import Redis
redis_conn = Redis()


@get('/pull/:pcid')
def pull(pcid):
	# send a url to slave
	pass 

@get('/push/:time')
def push(time):
	# cookie=urls???
	pass	
