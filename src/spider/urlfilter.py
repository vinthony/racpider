from urlparse import urlparse
from config.getconfig import getconfig
import socket
import random
def thisclient(url):
	c = getconfig()
	u = urlparse(url)
	try:
		ip = socket.gethostbyname(u.netloc)
	except Exception, e:
		ip = "0.0.0.0"
	if random.random() > 0.5:
		return True
	else:
		return False

def notinthisclient(url):
	return not thisclient(url)			 

def getrobot(content,robots,host):
	contents = content.split("\r\n")
	for item in contents:
		if item.strip().startswith("Disallow:"):
			search = item.split(":")[1]
			if search not in robots[host]:
				robots[host].append(search)	
	return robots			

