from urlprase import urlprase
from config.getconfig import getconfig
import socket
def thisclient(url):
	c = getconfig()
	u = urlprase(url)
	ip = socket.gethostbyname(o.netloc)
	if ip.endswith("1"):
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

