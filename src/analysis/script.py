from bs4 import BeautifulSoup
import re

class Items(object):
	def __init__(self):
		self.name = 'jandan'
	def filter(self,url):
		self.regexp = 'jandan.net/author'
		pattern = re.complie(self.regexp)
		if pattern.search(pattern):
			return True
		return False
			
	def parse(self,content):
		soup = BeautifulSoup(content)	
		print soup.title.name