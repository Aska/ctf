# PicoCTF 2017- Level 2 - Cryptography 2

**Title:** LeakedHashes  
**Category:** Cryptography  
**Points:** 90  
**Description:**

>Someone got hacked! Check out some service's password hashes that were leaked at [hashdump.txt](hashdump.txt)! Do you think they chose strong passwords? We should check... The service is running at shell2017.picoctf.com:61096!  

**Hint:**

>See if you can crack any of the login credentials and then connect to the service as one of the users. What's the chance these hashes have actually already been broken by someone else? Are there websites that host those cracked hashes? Connect from the shell with nc.

## Solution

Here's the [list](pwddump.txt) of cracked hash. Every md5 hash have been found except the one of the root.  
>$ nc shell2017.picoctf.com:61096  
>enter username:  
>lindsey  
>lindsey's password:sp337  
>welcome to shady file server. would you like to access the cat ascii art database? y/n  
>y  

Within the text output we can find: `flag is 1ae2d736242e28658d08e8b47dbf49bf`  

Thus the answer is `1ae2d736242e28658d08e8b47dbf49bf`