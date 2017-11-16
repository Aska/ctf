# PicoCTF 2017- Level 2 - Miscellaneous 2

**Title:** Mystery Box  
**Category:** Miscellaneous  
**Points:** 60  
**Description:**

>You've found a mystery machine with a sticky [note](note.txt) attached to it! Oh, there's also this [picture](MysteryBox.png) of the machine you found.  

**Hint:**

>It really gets your gears Turing.  
>I hear there's something Naval about it.  

## Solution

This one has a bit of historical touch since we have to decode a message encrypted with Enigma. Luckily for us we have the encryption parameters in the note and a lot of websites allow us to decrypt Enigma's messages.  
This [website](http://enigma.louisedade.co.uk/enigma.html) gives us the following result:  
>QUIT EPUZ ZLIN GIND EED  

The flag is `QUITEPUZZLINGINDEED`