# PicoCTF 2017- Level 1 - Reverse Engineering 1

**Title:** Hex2Raw  
**Category:** Reverse Engineering  
**Points:** 20  
**Description:**

>This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/33432c6de9329bca3a3ff26e5538d8f2 and turn that Hex2Raw!

**Hint:**

>Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

## Solution

First let's try to run the program:  
	$ cd /problems/9177bfe904b2fb486bf2063954b4b3cb
	$ ./hex2raw
	Give me this in raw form (0x41 -> 'A'):
	59c51289ace9cdd4004afa54d297d310

	You gave me:

The task here is to send an unprintable character to the program. The easiest way to do it in this environnement is to use python:  

	$ python -c "print('59c51289ace9cdd4004afa54d297d310'.decode('hex'))" | ./hex2raw
	Give me this in raw form (0x41 -> 'A'):                        
	59c51289ace9cdd4004afa54d297d310                               
	                                                               
	You gave me:                                                   
	59c51289ace9cdd4004afa54d297d310                               
	Yay! That's what I wanted! Here be the flag:                   
	95fbb12ef65fbea5c746f262292dc3c7          

The flag for this problem is `95fbb12ef65fbea5c746f262292dc3c7`