# PicoCTF 2017- Level 1 - Miscellaneous 5

**Title:** Leaf of the Forest  
**Category:** Miscellaneous  
**Points:** 30  
**Description:**

>We found an even bigger directory tree hiding a flag starting at /problems/7d91c03dff81a9c95bffb6d69358c92d. It would be impossible to find the file named flag manually...  

**Hint:**

>Is there a search function in Linux? Like if I wanted to 'find' something...  

## Solution

After some tries it seems that the correct file DOES NOT contains the word `flag`. So let's just use grep:  
	$ cd /problems/db39b5c002d8445dc6d2bbf49a8ccc37
	$ grep -r -v "flag" .
	c99501b0fe95402ed1c9191102fe1b68

The solution is `c99501b0fe95402ed1c9191102fe1b68`