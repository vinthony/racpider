import datetime
class Dict(dict):
    '''
    Simple dict but support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    >>> d3 = Dict(('a', 'b', 'c'), (1, 2, 3))
    >>> d3.a
    1
    >>> d3.b
    2
    >>> d3.c
    3
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

class HTMLModel(object):
	def __init__(self, **args):
		self.collection = dict()
		for (key,value) in args.iteritems():
			self.collection[key] = value

	def format(self):
		self.collection["date"] = datetime.datetime.utcnow()
		return self.collection

class URL(Dict):
	def __cmp__(self,other):
		if not self.priority:
			self.priority = 0
		if not other.priority:
			other.priority = 0
		return cmp(self.priority,other.priority)
		
if __name__ == '__main__':
	print HTMLModel(name="2",age="3").format()["name"]			
	print URL(dict(priority=100,w=12))