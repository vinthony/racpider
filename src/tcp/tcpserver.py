import socket
from utils import log
from utils import isjson
from SocketServer import TCPServer ,ThreadingMixIn,StreamRequestHandler


class SetupServer(StreamRequestHandler):
	def handle(self):
		self.data = self.request.recv(2<<10).strip()
		self.request.sendall()
						

def setupserver(server,port,urldistributer,rclient):
	sock = socket.socket(socket.AF_INIT,socket.SOCK_STREAM)
	sock.bind(server,int(port))
	sock.listen(20)
	retrytime = 0
	while True:
		connection,address = sock.accpet()
		log.info("client connection = %s,address = %s. " % (connection,address))
		try:
			connection.settimeout(5)#time out
			buf = connection.recv(2<<10) # buf is a json object
			if isjson(buf) == 0: # no error
				sock.sendall(urldistributer)
			else:
				#retry
				if retrytime < 3:
					retrytime += 1
				else:
					connection.close()
					retrytime = 0
		except socket.timeout:
			#bind unreach in urldistributer(redis)		
			rclient.set(address,404)
		connection.close()	