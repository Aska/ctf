# PicoCTF 2017- Level 0 - Tutorial 1

**Title:** Find the Middlename  
**Category:** Tutorial  
**Points:** 0  
**Description:**

>How can you figure out Robin Morris's middle name? Thankfully you have a [list](contractors.txt) you can check!

**Hint:**

>Please don't search by hand!  

## Solution
The solution is pretty straightforward using `grep`:  


    $ grep -i -E "^Robin [a-z]* Morris$" ./contractors.txt 
    Robin Almay Morris

Thus the first answer is `Almay`.