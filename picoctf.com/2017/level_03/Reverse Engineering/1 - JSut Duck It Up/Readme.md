# PicoCTF 2017- Level 3 - Reverse Engineering 1

**Title:** JSut Duck It Up  
**Category:** Reverse Engineering  
**Points:** 100  
**Description:**

>What in the world could this be?!?! [file](file)  

**Hint:**

>Maybe start searching for uses of these chunks of characers? Is there anything on the Internet with them?  

## Solution

A look at the page of [Esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language) on wikipedia tells us that the file is JSfuck code. After going to the [official JSfuck webpage](http://www.jsfuck.com/) and using the interpreter there, we get the flag.  

The flag is `aw_yiss_ducking_breadcrumbs_61637ee8`