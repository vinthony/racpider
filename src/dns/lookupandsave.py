from redistool import rclient
from urlprase import urlprase
import socket

def saveaddr(url,father=None):
	rc = rclient()
	o = urlprase(url)
	host = o.netloc
	ip = socket.gethostbyname(o.netloc)
	port = o.port
	search = o.path
	priority = getpriority(url)
	if father:
		depth = rc.get(father).depth +1
	else:		
		depth = 1
	rc.set(url,dict(host=host,ip=ip,port=port,search=search,priority=priority,depth=depth))	
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
	pro = 1000 - len(urlprase(url).host) - len(urlprase(url).path)
	if url.endswith('.html'):
		pro += 2
	if any(s in url for s in ("main","key","page","com","article")):
		pro += 10

	return pro		
