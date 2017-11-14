# PicoCTF 2017- Level 0 - Tutorial 2

**Title:** Dearest Ambition  
**Category:** Tutorial  
**Points:** 0  
**Description:**

>Robin handed me [this](message.txt) the other day. Maybe it will help me find the answer?

**Hint:**

>There are a number of solvers on the internet that can help!  

## Solution

By openning the text file we can see that Robin used ROT13 to encode his message. We could use any ROT13 decoder on the web but we can also use the terminal:  

	$ echo "Lb, fb unir lbh orra cynlvat gung arj Zrfbcrgf tnzr? Gubfr arj Zrtnybalpuvqnr naq Oenqlcbqvqnr gurl nqqrq ner cerggl pbby. Npghnyyl, V jbhyq tb nf sne nf fnlvat gung vg vf abj zl yvsr'f qrnerfg nzovgvba gb bognva n \"Vasyngnoyr Fybgu Zbafgre\"!" | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

And the result is:  

	Yo, so have you been playing that new Mesopets game? Those new Megalonychidae and Bradypodidae they added are pretty cool. Actually, I would go as far as saying that it is now my life's dearest ambition to obtain a "Inflatable Sloth Monster"!



The answer is `Inflatable Sloth Monster`