#!/usr/bin/env python

import json,sys
sys.path.append("/Users/nantu/projects/racpider/src/")
from utils import utils
def getconfig():
	dcfile = open("/Users/nantu/projects/racpider/src/config/default_config.json","r+")
	default_config = json.loads(dcfile.read())
	dcfile.close()
	userfile = open("/Users/nantu/projects/racpider/Racpider.json","r+")
	user_config = json.loads(userfile.read())
	userfile.close()
	return utils.mergejson(default_config,user_config)


if __name__ == '__main__':
	print json.dumps(getconfig())

