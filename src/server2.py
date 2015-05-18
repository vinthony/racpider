import SocketServer
from tcp.tcpserver import Server
from utils import log
# from redistool import rclinet
# from urls.urldistributer import urldistributer

def main():
	HOST,PORT = "localhost",23333
	server = SocketServer.ThreadingTCPServer((HOST,PORT),Server)
	log.info("start tcp server ,waiting for connection...")
	server.serve_forever()


if __name__ == '__main__':
	main()	