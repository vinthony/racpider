#!/usr/bin/env python
import json,sys,os

def mergejson(base,addition):
	re = base
	for (key,value) in addition.iteritems():
		if type(value) == type({}):#dict
			re[key] = mergejson(base[key],value)
		elif len(value) == 0 : # None	
			re[key] = base[key]
		else:
			re[key] = value
	return re

def getconfig():
	base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir,os.pardir,os.pardir))
	dir_name = os.path.dirname(os.path.abspath(__file__))
	dcfile = open(dir_name+"/default_config.json","r+")
	default_config = json.loads(dcfile.read())
	dcfile.close()
	userfile = open(base_dir+"/Racpider.json","r+")
	user_config = json.loads(userfile.read())
	user_config["src"] = os.path.abspath(os.path.join(base_dir,"src"))
	user_config["project_root"] = os.path.abspath(os.path.join(base_dir,"src"))
	userfile.close()
	return mergejson(default_config,user_config)


if __name__ == '__main__':
	print json.dumps(getconfig())
