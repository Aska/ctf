# PicoCTF 2017- Level 1 - Cryptography 4

**Title:** ComputeAES  
**Category:** Cryptography  
**Points:** 50  
**Description:**

>You found [this clue](clue.txt) laying around. Can you decrypt it?

**Hint:**

>Try online tools or python

## Solution

There are many way to decrypt an AES cipher with the key. I've coded a [minimalist python](compute_aes.py) file to decrypt the string:

```python
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
```
Which gave us the result:  
	flag{do_not_let_machines_win_83f2aeea}__________

Thus the answer is `do_not_let_machines_win_83f2aeea`