import datetime

class HTMLModel(object):
	def __init__(self, **args):
		self.collection = dict()
		for (key,value) in args.iteritems():
			self.collection[key] = value

	def format(self):
		self.collection["date"] = datetime.datetime.utcnow()
		return self.collection

if __name__ == '__main__':
	print HTMLModel(name="2",age="3").format()["name"]			