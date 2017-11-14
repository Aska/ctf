#! /usr/bin/env python3
from Cryptodome.Cipher import AES
import base64

def ecbDecrypt(data,key):
    obj = AES.new(key, AES.MODE_ECB)
    decrypted = obj.decrypt(data)
    return decrypted

cipher = base64.b64decode(b'Q69htRlf08tHHf1cJYcqIwteyQK8BdSDg9UihLpVOypNMEbpaG+kGrTKkch6y1Ab')
key = base64.b64decode(b'MWo1Z9kJZ60a4skUlfcENA==')

result = ecbDecrypt(cipher,key)
print(result.decode())