#!/usr/bin/env python
import requests
import sys
sys.path.append("/home/nantu/dev/racpider/src")
sys.path.append("/Users/nantu/projects/racpider/src")
from spider.geturlsfromlink import getlinks 
# config server ip:port
url = "http://192.168.31.110:5237"
url = "http://10.170.48.53:5237"
def notempty():
	e = requests.get(url+"/empty")
	if e.status_code != 200:
		return False
	if int(e.text) > 0 :
		return True
	return False	

while notempty():
	r = requests.get(url+"/pull")
	if r.status_code != 200:
		print "error"
	links = getlinks(r.text)
	files = {'file':",".join(links)}
	r2 = requests.get(url+"/push",headers=files)
	if r2.status_code != 200:
		break

