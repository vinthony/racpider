#!/usr/bin/env python
import requests
import sys
sys.path.append("/home/nantu/dev/racpider/src")
from spider.geturlsfromlink import getlinks 
# config server ip:port
def notempty():
	e = requests.get("http://192.168.31.110:5237/empty")
	if int(e.text) > 0 and r.status_code == 200:
		return True
	return False

while notempty():
	r = requests.get("http://192.168.31.110:5237/pull")
	if r.status_code != 200:
		print "error"
	links = getlinks(r.text)
#print links
	files = {'file':",".join(links)}
	r2 = requests.post("http://192.168.31.110:5237/push",headers=files)
	if r2.status_code != 200:
		break

