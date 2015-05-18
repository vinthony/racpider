import socket
from utils import log
from utils.isjson import isjson
import SocketServer

class Server(SocketServer.BaseRequestHandler):
	def headle(self):
		log.info("client connection = %s,address = %s. " % (connection,address))
		while True:
			pass
		