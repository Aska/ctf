# PicoCTF 2017- Level 3 - Reverse Engineering 3

**Title:** Much Ado About Hacking  
**Category:** Reverse Engineering  
**Points:** 165  
**Description:**

>In a lonely file, you find [prose](MuchAdoAboutHacking.spl) written in an interesting style. What is this Shakespearean play? What does it have to say? How could one get it to produce this [ending](ending.txt)?  

**Hint:**

>Some would say that Shakespearean english is an... esoteric language  
>I swear that this play compiles. However, there are different versions of the shakespeare language. If you get errors when you run spl2c on MuchAdoAboutHacking, then you need to use a different version of the language. There is a fixed version of the language here: https://stackoverflow.com/questions/1948372/compiling-and-executing-the-shakespeare-programming-language-translator-spl2c-on  

## Solution

The `MuchAdoAboutHacking.spl` file is a source written in [Shakespeare Programming Language](https://en.wikipedia.org/wiki/Shakespeare_Programming_Language). Here's the python interpreter we will use: [shakespearlang](https://github.com/zmbc/shakespearelang).  
    $ shakespeare run MuchAdoAboutHacking.spl
    Its@MidSuMm3rNights3xpl0!t

Thus the flag is `Its@MidSuMm3rNights3xpl0!t`