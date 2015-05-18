import SocketServer
from tcp.tcpserver import SetupServer
from redistool import rclinet
from urls.urldistributer import urldistributer

def main():
	HOST,PORT = "localhost",23333
	server = SocketServer.TCPServer((HOST,PORT),SetupServer)
	server.serve_forever()