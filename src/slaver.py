#!/usr/bin/env python
import requests
import sys,time
import socket
from spider.geturlsfromlink import getlinks 
from spider.mongoc import MongoC
from spider.urlfilter import thisclient,notinthisclient
from spider.priorityQueue import addtoQueue,deQueueURL
from config.getconfig import getconfig
STATUS_OK = 200
config = getconfig()
url = "http://"+config["server"]["host"]+":"+config["server"]["port"]
q = []
regexps  = {}
def getidentify():
	return socket.gethostname()
# make sure
def notempty():
	try:
		data = {"client":getidentify(),"count":MongoC().count(),"network":}
		e = requests.get(url+"/empty",headers=data,timeout=1)
	except requests.exceptions.Timeout:
		return False
	if e.status_code != STATUS_OK:
		return False
	if int(e.text) > 0 :
		print "remainer:"+e.text
		return True
	return False	

## 客户端一直进行检验，并且发送客户端的状态到服务器。
def slaver_client():
	while notempty():
		if int(config["sleep"]) > 0: ##礼貌策略
			time.sleep(int(config["sleep"]))
		r = requests.get(url+"/pull")
		if r.status_code != STATUS_OK:
			print "error"
		addtoQueue(h,obj=json.dumps(r.text))
		links = getlinks(deQueueURL(h))
		for x in filter(thisclient,links):
			addtoQueue(h,x,r.text)
		l = filter(notinthisclient,links)
		files = {'file':",".join(l)}
		r2 = requests.get(url+"/push",headers=files)
		if r2.status_code != STATUS_OK:
			break
if __name__ == "__main__":
	slaver_client()
