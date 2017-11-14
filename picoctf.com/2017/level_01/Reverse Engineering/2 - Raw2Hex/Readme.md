# PicoCTF 2017- Level 1 - Reverse Engineering 1

**Title:** Raw2Hex  
**Category:** Reverse Engineering  
**Points:** 20  
**Description:**

>This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/45f3b0abcf176b7cf7c1536b28d05d72 and turn that Raw2Hex!

**Hint:**

>Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

## Solution

First let's try to run the program:  
	$ /problems/854399173cf870506ff3a4397adfefc1/raw2hex
	The flag is::ϱ←=B2π▒┐▒@░␊┌┌↑┬␊␉:/␉┌␊└/854399173␌°87█5█6
	°°3▒4397▒␍°␊°␌1$

Here we need to get the output of the raw2hex program and convert it to hexadecimal to get our flag. Again we will use python:  
	$ /problems/854399173cf870506ff3a4397adfefc1/raw2hex > hex2raw.txt
	$ python
	>>> print(open('./hex2raw.txt').readline()[12:].encode('hex'))
	0e3ab3cfb1a7db2c3d18428532c97b05

In the first line we save the content of the program into a text file, then we start the python interpreter.
The python command is quite simple : we open our text file, we read the first line, we keep only the characters after the 12 first ones (to remove "The flag is::") and we encode what we have in hex.  

Then the flag is `0e3ab3cfb1a7db2c3d18428532c97b05`