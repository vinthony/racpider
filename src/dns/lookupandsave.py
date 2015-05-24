from redistool import rclient
from urlparse import urlparse
import socket,json
def geturldict(url,father=None):
	o = urlparse(url)
	host = o.netloc
	try:
		ip = socket.gethostbyname(o.netloc)	
	except Exception, e:
		ip = "0.0.0.0"
	port = o.port or 80
	search = o.path
	priority = getpriority(url)
	if father:
		depth = rc.get(father).depth +1
	else:		
		depth = 1
	return dict(host=host,ip=ip,port=port,search=search,priority=priority,depth=depth)

def saveaddr(url,father=None):
	rc = rclient()
	rc.set(url,geturldict(url))	
	return True

def choosenode(url):
    #choose a node from urls	
    rc = rclient()
    o = rc.get(url)
    if o.ip.endswith("2"):
    	return "node1"
    if o.ip.endswith("1"):
    	return "node2"	

def getpriority(url):
	pro = 1000 - len(urlparse(url).netloc) - len(urlparse(url).path)
	if url.endswith('.html'):
		pro += 2
	if any(s in url for s in ("main","key","page","com","article")):
		pro += 10

	return pro		
