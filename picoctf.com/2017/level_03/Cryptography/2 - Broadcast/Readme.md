# PicoCTF 2017- Level 3 - Cryptography 2

**Title:** Broadcast  
**Category:** Cryptography  
**Points:** 120  
**Description:**

>You stumbled upon a group [Message](clue.txt). Can you figure out what they were sending? The string sent is ascii encoded as a hex number (submit the ascii string as the flag)  

**Hint:**

>The same message, with a small exponent, is being encrypted with several different n values  

## Solution

Given the name of the problem and the clue, it seems that we will have to use a [Håstad's broadcast attack](https://en.wikipedia.org/wiki/Coppersmith's_attack#H.C3.A5stad.27s_broadcast_attack). This attack work if `e = 3` and requires at least 3 identical messages, which gives us the following mathematical formula:  
    c<sub>1</sub> ≡ m<sup>3</sup> mod N<sub>1</sub>  
    c<sub>2</sub> ≡ m<sup>3</sup> mod N<sub>2</sub>  
    c<sub>3</sub> ≡ m<sup>3</sup> mod N<sub>3</sub>  

Now if we use the [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem), we can find `x`:
    x ≡ m<sup>3</sup> mod N<sub>1</sub>N<sub>2</sub>N<sub>3</sub>  

Which gives us:  
    x = m<sup>3</sup>  
    m = $\sqrt[3]{x}$  

After creating a [simple python script](hastad_attack.py), we get the flag: `broadcast_with_small_e_is_killer_86029531745`