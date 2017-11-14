# PicoCTF 2017- Level 1 - Cryptography 3

**Title:** Hash101  
**Category:** Cryptography  
**Points:** 50  
**Description:**

>Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:9661

**Hint:**

>All concepts required to complete this challenge, including simple modular math, are quickly found by googling :)

## Solution

Given the port number, let's connect with `netcat`:  
	$ nc shell2017.picoctf.com 56120

	Welcome to Hashes 101!

	There are 4 Levels. Complete all and received a prize!

	-------- LEVEL 1: Text = just 1's and 0's --------
	All text can be represented by numbers. To see how different letters translate t
	o numbers, go to http://www.asciitable.com/

	TO UNLOCK NEXT LEVEL, give me the ASCII representation of 0111011101101111011100100110110001100100
	0111011101101111011100100110110001100100

This first level is quite easy: 0111011101101111011100100110110001100100 translate to "world" in Ascii  

	$ Correct! Completed level 1

	------ LEVEL 2: Numbers can be base ANYTHING -----
	Numbers can be represented many ways. A popular way to represent computer data i
	s in base 16 or 'hex' since it lines up with bytes very well (2 hex characters =
	 8 binary bits). Other formats include base64, binary, and just regular base10 (
	decimal)! In a way, that ascii chart represents a system where all text can be s
	een as "base128" (not including the Extended ASCII codes)

	TO UNLOCK NEXT LEVEL, give me the text you just decoded, world, as its hex equiv
	alent, and then the decimal equivalent of that hex number ("foo" -> 666f6f -> 67
	13199)

world -> 77 6f 72 6c 64 -> 512970878052

	$ hex>776f726c64
	Good job! 776f726c64 to ASCII -> world is world
	Now decimal
	dec>512970878052
	Good job! 512970878052 to Hex -> 776f726c64 to ASCII -> world is world
	Correct! Completed level 2

	----------- LEVEL 3: Hashing Function ------------
	A Hashing Function intakes any data of any size and irreversibly transforms it t
	o a fixed length number. For example, a simple Hashing Function could be to add
	up the sum of all the values of all the bytes in the data and get the remainder
	after dividing by 16 (modulus 16)

	TO UNLOCK NEXT LEVEL, give me a string that will result in a 1 after being tran
	sformed with the mentioned example hashing function

	>1
	Correct! Completed level 3

This one was just pure luck. I suppose we are supposed to logically guess how to find a corresponding number.

	$ --------------- LEVEL 4: Real Hash ---------------
	A real Hashing Function is used for many things. This can include checking to en
	sure a file has not been changed (its hash value would change if any part of it
	is changed). An important use of hashes is for storing passwords because a Hashi
	ng Function cannot be reversed to find the initial data. Therefore if someone st
	eals the hashes, they must try many different inputs to see if they can "crack"
	it to find what password yields the same hash. Normally, this is too much work (
	if the password is long enough). But many times, people's passwords are easy to
	guess... Brute forcing this hash yourself is not a good idea, but there is a str
	ong possibility that, if the password is weak, this hash has been cracked by som
	eone before. Try looking for websites that have stored already cracked hashes.

	TO CLAIM YOUR PRIZE, give me the string password that will result in this MD5 ha
	sh (MD5, like most hashes, are represented as hex digits):
	89cfc208ee100d1d4895d4bf3ca6310c

	>m47ch
	Correct! Completed level 4
	You completed all 4 levels! Here is your prize: 605911fee24de43af8ebe50ec7d210ec

For this one we need to use a database since md5 hashing is not reversible. [Crackstation.net](https://crackstation.net) gave us the result.

The answer is `605911fee24de43af8ebe50ec7d210ec` (which is the md5 for 644293066153, which is the decimal for hex value 9602DBFDA9, which isn't corresponding to any word...).