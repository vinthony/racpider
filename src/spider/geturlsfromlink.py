import requests
import io,sys,os
import time
from urllib import unquote
from status import NetworkStatus
sys.path.append("/Users/nantu/projects/racpider/src/")
from utils import log
from downloader import Downloader
from getlinks import getdoclinks

def getlinks(url):
	return getdoclinks(Downloader("name",url.split("/")[-1],url).get()).parse()
