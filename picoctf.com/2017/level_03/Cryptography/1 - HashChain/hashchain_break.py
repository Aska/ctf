#! /usr/bin/python
import hashlib
import json

seed = b'2633'
result = b'9e7093cade6e3df310198186f9ede082'

hash = hashlib.md5(seed).hexdigest().encode()
previous = seed

while(hash != result):
	previous = hash
	hash = hashlib.md5(hash).hexdigest().encode()
	
print("Try to input", previous.decode())