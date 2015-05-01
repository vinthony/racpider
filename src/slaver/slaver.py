import requests
import sys
sys.path.append("..")
from spider.geturlsfromlinks import getlinks 
# config server ip:port
r = requests.get(server.url)
if r.status_code != 200:
	log.warning("error:"+str(r.status_code)+":"+str(self.url))
#doing the spider job
# url in body?
links = getlinks(r.text)



