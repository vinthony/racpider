from pymongo import MongoClient
from config.getconfig import getconfig

config = getconfig()
mc = config['mongodb']
client = MongoClient(mc['host'],int(mc['port']))