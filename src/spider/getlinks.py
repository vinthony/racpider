#!/usr/bin/env python

from bs4 import BeautifulSoup
import re
_REP_IS_FORMAT_URL = "http"

def html_filter(item):
	if type(item)!= type("str"):
		return False
	if item.startswith("http"):
		return True
	else:
		return False	


class getdoclinks(object):
	def __init__(self, body):
		self.soup = BeautifulSoup(body)

	def parse(self):
		m = [links.get('href') for links in self.soup.find_all('a')]
		a_links = filter(html_filter,m)
		frames = [fra.get('src') for fra in self.soup.find_all('frame')]
		return a_links

