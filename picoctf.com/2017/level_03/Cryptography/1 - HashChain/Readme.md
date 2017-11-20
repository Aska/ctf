# PicoCTF 2017- Level 3 - Cryptography 1

**Title:** HashChain  
**Category:** Cryptography  
**Points:** 90  
**Description:**

>We found a service hiding a flag! It seems to be using some kind of MD5 Hash Chain authentication to identify who is allowed to see the flag. Maybe there is a flaw you can exploit? [hcexample.py](hcexample.py) has some example code on how to calculate iterations of the MD5 hash chain. Connect to it at shell2017.picoctf.com:58801!  

**Hint:**

>Connect from the shell with nc. Read up on how Hash Chains work and try to identify what could make this cryptosystem weak.  

## Solution

First, let's check the service given to us:  
```bash
$ nc shell2017.picoctf.com 58801

*******************************************
***            FlagKeeper 1.1           ***
*  now with HASHCHAIN AUTHENTICATION! XD  *
*******************************************

Would you like to register(r) or get flag(f)?

r/f?

r
Hello new user! Your ID is now 4208 and your assigned hashchain seed is 4a71e49f
6bda0c9b7642f39f1aa1f567
Please validate your new ID by sending the hash before this one in your hashchai
n (it will hash to the one I give you):
01148c10c2ecca7a2107779753994107
```
We can notice that the hashchain seed is the `md5` of the given `ID`:  
    md5(4208) = 01148c10c2ecca7a2107779753994107  

Let's check the `get the flag` option:

```bash
$ nc shell2017.picoctf.com 58801

*******************************************
***            FlagKeeper 1.1           ***
*  now with HASHCHAIN AUTHENTICATION! XD  *
*******************************************

Would you like to register(r) or get flag(f)?

r/f?

f
This flag only for user 5972
Please authenticate as user 5972
af3664063d48ddde05d6ee424d1b027d
Next token?
a
That doesn't hash to what I gave you... No flag for you!
```

So what we can guess is that we need to hash multiple times the `user ID` until we find the `md5` given to us. Then, the penultimate hash will be the one to enter. Once done in [python](hashchain_break.py), let's try the result:  


```bash
$ nc shell2017.picoctf.com 58801
*******************************************
***            FlagKeeper 1.1           ***
*  now with HASHCHAIN AUTHENTICATION! XD  *
*******************************************

Would you like to register(r) or get flag(f)?

r/f?

f
This flag only for user 2633
Please authenticate as user 2633
9e7093cade6e3df310198186f9ede082
Next token?
38be583dfe185fd1fd253e105a2930ef
Hello user 2633! Here's the flag: 9494f4171092452602fa545ab927e99e

```


The flag is `9494f4171092452602fa545ab927e99e`