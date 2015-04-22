#!/usr/bin/env python

def mergejson(base,addition):
	re = dict()
	for (key,value) in addition.iteritems():
		if type(value) == type({}):#dict
			re[key] = mergejson(base[key],value)
		elif len(value) == 0 : # None	
			re[key] = base[key]
		else:
			re[key] = value
	return re