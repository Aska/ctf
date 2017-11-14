#! /usr/bin/env python3

import socket
import re

def netcat(host, port):
	s = socket.socket()
	s.connect((host, int(port)))

	data = s.recv(4096).decode("utf-8")
	print(data)

	char = str.encode(re.findall(r'give me the \'(.*?)\' character', repr(data))[0])
	repeat = str.encode(re.findall(r'character \'(.*?)\' times,', repr(data))[0])
	endchar = str.encode(re.findall(r'a single \'(.*?)\'\.', repr(data))[0])

	answer = char*int(repeat)+endchar+b'\n'
	s.send(answer)

	print(s.recv(4096).decode("utf-8"))


netcat('shell2017.picoctf.com', '44840')