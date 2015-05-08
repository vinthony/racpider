#!/usr/bin/env python
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import re
_REP_IS_FORMAT_URL = "http"

def html_filter(item):
	if type(item)!= type(u"unicode"):
		return False
	if item.startswith("http"):
		return True
	else:
		return False

def sharp_mapper(item):
	if item.find('#')>0:
		return item.split('#')[0].encode('utf-8')
	else:
		return item.encode('utf-8')

class getdoclinks(object):
	def __init__(self, body):
		if body is not None:
			self.soup = BeautifulSoup(body)
		else:
			self.soup = None	

	def parse(self):
		if self.soup is None:
			return []
		m = [ x.get('href') for x in self.soup.find_all('a')]
		a_links = map(sharp_mapper,filter(html_filter,m))
		frames = [fra.get('src') for fra in self.soup.find_all('frame')]
		return a_links

