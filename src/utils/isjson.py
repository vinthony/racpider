import json

def isjson(s):
	j = json.loads(s)
	if isinstance(json,dict) or isinstance(j,list):
		return True
	return False	