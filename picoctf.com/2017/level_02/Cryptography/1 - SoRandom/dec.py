#!/usr/bin/python
import random,string

def decryptFlag(flag):
	random.seed("random")
	decflag = ""
	for c in flag:
		if c.islower():
			decflag += chr((ord(c) - ord('a') - random.randrange(0,26))%26 + ord('a'))
		elif c.isupper():
			decflag += chr((ord(c) - ord('A') - random.randrange(0,26))%26 + ord('A'))
		elif c.isdigit():
			decflag += chr((ord(c) - ord('0') - random.randrange(0,10))%10 + ord('0'))
		else:
			decflag += c
	return decflag

flag = "BNZQ:3o8b2bgl0689u4aj640407963277k0fc"
print(decryptFlag(flag))
