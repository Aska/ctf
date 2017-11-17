# PicoCTF 2017- Level 2 - Master Challenge

**Title:** Missing Identity  
**Category:** Master Challenge  
**Points:** 100  
**Description:**

>Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one [file](file) and find the flag. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out. The flag starts with the character z.  

**Hint:**

>What file is this?  
>What do you expect to find in the file structure?  
>All characters in the file are lower case or numberical. There will not be any zeros.  

## Solution

# Easy Way

After looking at the raw bytes of the file, it seems that it is a compress archive containing multiple images.  
Let's try to unzip it:
	$ unzip ./file  
	$ ls -l  
	total 788  
	-rw-r--r-- 1 aska vr-gear-console_4 403552 Mar 31  2017 file  
	-rw-r--r-- 1 aska aska                   0 Mar 31  2017 flag.png  
	-rw-r--r-- 1 aska aska               63671 Mar 31  2017 nottheflag1.png  
	-rw-r--r-- 1 aska aska               58401 Mar 31  2017 nottheflag2.png  
	-rw-r--r-- 1 aska aska               61592 Mar 31  2017 nottheflag3.png  
	-rw-r--r-- 1 aska aska               58515 Mar 31  2017 nottheflag4.png  
	-rw-r--r-- 1 aska aska               60308 Mar 31  2017 nottheflag5.png  
	-rw-r--r-- 1 aska aska               61838 Mar 31  2017 nottheflag6.png  

It seems that `flag.png` return the error: `bad zipfile offset (local header sig):  0`

By simply open the file in an hex editor we can notice that the 6 first bytes are replaced by `56 56 56 56 56 56` (`X X X X X X` in ascii). We can recreate the zip file signature by replacing the 4 first bytes by `50 4B 03 04` and then unzip the [file.zip] without error.


The flag is `zippidydooda92849522`