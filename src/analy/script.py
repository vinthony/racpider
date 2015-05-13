from bs4 import BeautifulSoup
import re

class Items(object):
	def __init__(self):
		self.name = 'jandan'
	def filter(self,url):
		self.regexp = 'jandan.net'
		pattern = re.compile(self.regexp)
		if pattern.search(url):
			return True
		return False
			
	def parse(self,content):
		soup = BeautifulSoup(content)	
		print soup.title