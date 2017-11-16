# PicoCTF 2017- Level 1 - Cryptography 5

**Title:** ComputeRSA  
**Category:** Cryptography  
**Points:** 50  
**Description:**

>RSA encryption/decryption is based on a formula that anyone can find and use, as long as they know the values to plug in. Given the encrypted number 150815, d = 1941, and N = 435979, what is the decrypted number?  

**Hint:**

>decrypted = (encrypted) ^ d mod N  

## Solution

This one is even easier than the previous one. [In python](compute_rsa.py):  

```python
#! /usr/bin/env python3

def rsaDecrypt(enc, d, N):
	return enc ** d % N

decrypted = rsaDecrypt(150815, 1941, 435979)
print(decrypted)
```
Which gave us the result:  
>133337  

Thus the answer is `133337`