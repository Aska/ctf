# PicoCTF 2017- Level 2 - Reverse Engineering 2

**Title:** Programmers Assemble  
**Category:** Reverse Engineering  
**Points:** 75  
**Description:**

>You found a text [file](assembly.s) with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df  

**Hint:**

>All of the commands can be found [here](https://en.wikipedia.org/wiki/X86_assembly_language) along with what they do.  
>It may be useful to be able to run the code, with test values.  

## Solution

Since we are supposed to work on a x86 system, when opening the `assembly.s` file, we have:  
```stack
.global main               |
                           |
main:                      |
    mov $XXXXXXX, %eax     |
    mov $0, %ebx           |  -> set %ebx to 0
    mov $0x8, %ecx         |  -> set %ecx to 0x8
loop:                      |
    test %eax, %eax        |
    jz fin                 |  -> call fin() if %eax == 0
    add %ecx, %ebx         |  -> add %ecx to %ebx
    dec %eax               |  -> decrease %eax
    jmp loop               |
fin:                       |
    cmp $0xf5f8, %ebx      |  -> call good() if %ebx == 0xf5f8
    je good                |
    mov $0, %eax           |  -> set %eax to 0
    jmp end                |
good:                      |
    mov $1, %eax           |  -> set %eax to 1
end:                       |
    ret                    |
                           |
```

Given the content of `loop`, we want to solve the following equation in such a way that `%ebx` equal 1:  
>%ebx   = %ecx * %eax  

But we know that in order to call `good`, we must have:  
>%ebx = 0xf5f8  

Now we can simplify:  
>0xf5f8 = 0x8 * %eax  
>%eax = 0xf5f8 / 0x8  
%eax  = 0x1ebf  

So the answer is `0x1ebf`