#! /usr/bin/env python3

def rsaDecrypt(enc, d, N):
	return enc ** d % N

decrypted = rsaDecrypt(150815, 1941, 435979)
print(decrypted)