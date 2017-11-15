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