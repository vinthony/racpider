#!/usr/bin/env python
import requests
import sys,time
from spider.geturlsfromlink import getlinks 
from config.getconfig import getconfig
STATUS_OK = 200
config = getconfig()
url = "http://"+config["server"]["host"]+":"+config["server"]["port"]

# make sure
def notempty():
	try:
		e = requests.get(url+"/empty",timeout=1)
	except requests.exceptions.Timeout:
		return False
	if e.status_code != STATUS_OK:
		return False
	if int(e.text) > 0 :
		print "remainer:"+e.text
		return True
	return False	

def slaver_client():
	while notempty():
		if int(config["sleep"]) > 0:
			time.sleep(int(config["sleep"]))
		r = requests.get(url+"/pull")
		if r.status_code != STATUS_OK:
			print "error"
		links = getlinks(r.text)
		files = {'file':",".join(links)}
		r2 = requests.get(url+"/push",headers=files)
		if r2.status_code != STATUS_OK:
			break
if __name__ == "__main__":
	slaver_client()
