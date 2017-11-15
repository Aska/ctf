# PicoCTF 2017- Level 2 - Forensics 2

**Title:** Little School Bus  
**Category:** Forensics  
**Points:** 75  
**Description:**

>Can you help me find the data in this [littleschoolbus.bmp](littleschoolbus.bmp)?

**Hint:**

>Look at least significant bit encoding!!

## Solution

This one is way more subtle that the previous one. Given the hint, we suppose that a message is hidden within the image using the [Least Significant Bit](https://en.wikipedia.org/wiki/Least_significant_bit) encoding. After trials and failures the following Python code gives us the result:  


```python
buffering = ''
bits = ''

with open("littleschoolbus.bmp", "rb") as file:
	bytesList = bytearray(file.read()) # store all the bytes in a byte array


# We don't know at which position the LSB have started to be distributed
for i in range(0, len(bytesList)):
	bytesList = bytesList[i:]
	for byte in bytesList:
		bits += str(byte & 1) # add the LSB to the bits list
		if(len(bits) == 8):
			char = chr(int(bits, 2))
			if(32 < ord(char) < 126): # store the char in our string only if readable
				buffering = buffering+char

			# prepare to collect a new byte
			bits = ''

	if("flag" in buffering):
		break
	else:
		buffering = ''

print(buffering[:45]) # print only the 45 first char of the string we got
```

Which gives us:  
	$./least_significant_bit.py
	flag{remember_kids_protect_your_headers_5e31}

Thus the answer is `remember_kids_protect_your_headers_5e31`