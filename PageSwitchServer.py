#! /usr/bin/env python
# -*- coding: utf-8 -*-  

# Echo server

import socket
# This try/except is necessary only for ease of testing on a server without the API
try:
	import DaVinciResolveScript
	#Instantiate Resolve object
	resolve = DaVinciResolveScript.scriptapp('Resolve')
except ImportError:
	pass

def listen():
	while True:
		c, addr = s.accept()
		print 'Got connection from', addr
		data = c.recv(32)
		print data
		if not data: break
		c.sendall(data)
		c.close()
		
		# Switch Resolve page if API is available
		try:
			resolve.OpenPage(data)
		except NameError:
			print 'Resolve API not found.'

def opencomm(port):
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((server, port))
	s.listen(1)

if __name__ == '__main__':

	# Assign server parameters
	server = '192.168.1.1'
	port   = 7779

	s = socket.socket()
	opencomm(port)
	listen()

