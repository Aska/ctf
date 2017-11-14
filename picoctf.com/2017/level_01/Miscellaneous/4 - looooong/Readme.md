# PicoCTF 2017- Level 1 - Miscellaneous 4

**Title:** looooong  
**Category:** Miscellaneous  
**Points:** 20  
**Description:**

>I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:44840?

**Hint:**

>Use the nc command to connect!  
>I hear python is a good means (among many) to generate the needed input.  
>It might help to have multiple windows open  

## Solution

First let's connect to the given port:  
	$ nc shell2017.picoctf.com 44840
	To prove your skills, you must pass this test.
	Please give me the 'n' character '725' times, followed by a single '4'.
	To make things interesting, you have 30 seconds.
	Input:
	WRONG!

Let's make a [python script](looooong.py) that will get the instructions from the server and answer automatically:

```python
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
```

$ ./looooong.py
To prove your skills, you must pass this test.
Please give me the 'K' character '585' times, followed by a single '3'.
To make things interesting, you have 30 seconds.
Input:

You got it! You're super quick!
Flag: with_some_recognition_and_training_delusions_become_glimpses_97b1f7514342008e75bd0238aa007d09

The solution is `with_some_recognition_and_training_delusions_become_glimpses_97b1f7514342008e75bd0238aa007d09`