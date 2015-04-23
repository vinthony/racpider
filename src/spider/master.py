from rq import Queue
from redis import Redis
from geturlsfromlink import getlinks
import time

redis_conn = Redis()

q = Queue(connection=redis_conn)
	
job = q.enqueue(getlinks,"http://news.qq.com")

while not job.result:
	pass

i = 0

for x in xrange(0,len(job.result)):
	if i > 1000:
		break;
	q.enqueue(getlinks,job.result[x])
	i = i + 1

print "all done"	