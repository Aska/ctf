# PicoCTF 2017- Level 2 - Cryptography 1

**Title:** SoRandom  
**Category:** Cryptography  
**Points:** 75  
**Description:**

>We found [sorandom.py](sorandom.py) running at shell2017.picoctf.com:63997. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?  
Update (text only) 16:16 EST 1 Apr Running python 2 (same version as on the server)  

**Hint:**

>How random can computers be?

## Solution

First, let's take a quick glance at the server. The page output is as follow:  
>Unguessably Randomized Flag: BNZQ:3o8b2bgl0689u4aj640407963277k0fc  

After checking the `sorandom.py` file, here a script to decode the randomized flag:  

```python
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
```

Because the `random` function gives different results depending on the computer it runs on (even if the `random.seed()` is the same), we need to run the script on the picoctf server. Which gives us:  

>$ ./dec.py  
>FLAG:0d6f1cac5615c7ae971761318430c9bb  

Thus the answer is `0d6f1cac5615c7ae971761318430c9bb`