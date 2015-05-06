#!/usr/bin/env python
import requests
import sys,time
from spider.geturlsfromlink import getlinks 
from config.getconfig import getconfig
STATUS_OK = 200
config = getconfig()
url = "http://"+config["server"]["host"]+":"+config["server"]["port"]

def notempty():
	e = requests.get(url+"/empty")
	if e.status_code != STATUS_OK:
		return False
	if int(e.text) > 0 :
		return True
	return False	

while notempty():
	r = requests.get(url+"/pull")
	if r.status_code != STATUS_OK:
		print "error"
	links = getlinks(r.text)
	files = {'file':",".join(links)}
	r2 = requests.get(url+"/push",headers=files)
	if r2.status_code != STATUS_OK:
		break

