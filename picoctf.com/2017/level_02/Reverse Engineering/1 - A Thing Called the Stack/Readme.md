# PicoCTF 2017- Level 2 - Reverse Engineering 1

**Title:** A Thing Called the Stack  
**Category:** Reverse Engineering  
**Points:** 60  
**Description:**

>A friend was stacking dinner plates, and handed you [this](assembly.s), saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df  

**Hint:**

>Where is the return address saved on the stack?  
>Which commands actually affect the stack?  

## Solution

Since we are supposed to work on a x86 system, when opening the `assembly.s` file, we have:  
```stack
foo:
    pushl %ebp              |  0x4
    mov %esp, %ebp          |
    pushl %edi              |  0x4
    pushl %esi              |  0x4
    pushl %ebx              |  0x4
    sub $0xb4, %esp         |  0xb4
    movl $0x1, (%esp)       |
    movl $0x2, 0x4(%esp)    |
    movl $0x3, 0x8(%esp)    |
    movl $0x4, 0xc(%esp)    |
```
Now we simply add up the values:  
>0x4+0x4+0x4+0x4+0xb4 = 0xc4  

Thus the answer is `0xc4`