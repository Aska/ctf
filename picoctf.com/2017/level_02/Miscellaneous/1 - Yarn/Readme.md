# PicoCTF 2017- Level 2 - Miscellaneous 1

**Title:** Yarn  
**Category:** Miscellaneous  
**Points:** 55  
**Description:**

>I was told to use the linux strings command on [yarn](yarn), but it doesn't work. Can you help? I lost the flag in the binary somewhere, and would like it back  

**Hint:**

>What does the strings command use to determine if something is a string?  
>Is there an option to change the length of what strings considers as valid?  

## Solution

As advised in the hint section, let's try to check the strings contained within the `yarn` file using the `strings` command with a `n` parameter of size 2:  
>$ strings -n 2 ./yarn  
>[...]  
>Sub  
>mit  
>_me  
>_fo  
>r_I  
>_am  
>_th  
>e_f  
>lag  
>[...]  

Thus flag is `Submit_me_for_I_am_the_flag`