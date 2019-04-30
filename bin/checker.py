#!/usr/bin/python3

import sys, configparser
from datetime import datetime
import socket, urllib.request
## PySocks
import socks
from sockshandler import SocksiPyHandler

TESTURI = "https://google.com/"
PROXYHOST = "127.0.0.1"
TIMEOUT = 30

## https://stackoverflow.com/a/14906787
class Logger(object):
	def __init__(self):
		self.terminal = sys.stdout
		self.log = open("result.txt", "w")

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		self.terminal.flush()

sys.stdout = Logger()

def checkproxy(port, type):
	if type == 'http':
		handler = socks.HTTP
	elif type == 'socks':
		handler = socks.SOCKS5
	elif type == 'http0':
		proxy = urllib.request.ProxyHandler({'http': PROXYHOST +':' + str(port)})
	else:
		print("[unsupported type]")
		return

	if type == 'http0':
		opener = urllib.request.build_opener(proxy)
	else:
		opener = urllib.request.build_opener(
			SocksiPyHandler(handler, PROXYHOST, port)
		)

	try:
		response = opener.open(TESTURI, timeout=TIMEOUT).read()
	except Exception as e:
		print("[%5s]" % ('dead'))
		return

	print("[%5s]" % ('alive'))

def main():
	# Read list with ports and information
	config = configparser.ConfigParser()
	config.read('list.ini')
	proxyList = config.sections()

	print("Started check at %s UTC" % (datetime.utcnow()))
	print("Types: HTTP - using SocksiPyHandler, HTTP0 - using urllib, SOCKS - only 5th version using SocksiPyHandler")
	print("[%5s] [%5s] [%60s] [%16s] [%16s] [%16s] [%5s]" %
		('PORT','TYPE','B32 ADDRESS','NAME','OWNER','INFO','STATUS'))

	for currentProxy in proxyList:
		tunnel = dict(config.items(str(currentProxy)))

		print(
			"[%5d] [%5s] [%60s] [%16s] [%16s] [%16s] " % (
				int(currentProxy),
				tunnel['type']    if ("type" in tunnel)    else "none",
				tunnel['address'] if ("address" in tunnel) else "",
				tunnel['name']    if ("name" in tunnel)    else "",
				tunnel['owner']   if ("owner" in tunnel)   else "",
				tunnel['info']    if ("info" in tunnel)    else ""
			),
			end='', flush=True
		)

		checkproxy(int(currentProxy), str(config[currentProxy]['type']))

if __name__ == '__main__':
	main()
