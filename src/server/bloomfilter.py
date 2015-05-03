#!/usr/bin/env python
from bitarray import bitarray

class BloomFilter(object):
	def __init__(self):
		DEFAULT_SIZE = 2**24
		self.seeds = [7,11,13,31,37,61]
		self.table = bitarray(DEFAULT_SIZE)
		self.func = list()
		for x in range(0,len(self.seeds)):
			self.func.append(Hash(DEFAULT_SIZE,self.seeds[x]))

	def add(self,value):
		if value:
			for f in self.func:
				self.table[f.hash(value)] = True

	def contains(self,value):
		if not value:
			return False
		ret = True
		for f in self.func:
			ret = ret and self.table[f.hash(value)]				
		return ret 

class Hash(object):
	def __init__(self, cap,seed):
		self.cap = cap
		self.seed = seed

	def hash(self,value):
		result = 0;
		lens = len(value)
		for x in range(0,lens):
			result = self.seed * result + ord(value[x])
		return ( self.cap - 1 ) & result
		

if __name__ == "__main__":
	bf = BloomFilter()
	bf.add("1234556.com")
	bf.add("123.com")
	print bf.contains("123ddd.com")