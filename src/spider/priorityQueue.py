from spider.models import URL
from urlpraser import urlpraser
from dns.lookupandsave import geturldict
import heapq
def addtoQueue(queue,url,father,obj=None):
	if obj:
		heappush(queue,URL(obj))
	else:
		heappush(queue,URL(geturldict(url),father))

def deQueue(queue):
	obj = heappop(queue)		
	return obj.host+obj.search