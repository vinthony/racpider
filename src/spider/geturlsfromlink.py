from downloader import Downloader
from getlinks import getdoclinks
from config.getconfig import getconfig
config = getconfig()
def getlinks(url):
	return getdoclinks(Downloader(config["name"],url.split("/")[-1],url).get()).parse()
