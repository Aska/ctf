# PicoCTF 2017- Level 1 - Forensics 1

**Title:** Digital Camouflage  
**Category:** Forensics  
**Points:** 50  
**Description:**

>We need to gain access to the school routers to cover our tracks. Let's try and see if we can find the password in the network data we captured earlier: [data.pcap](data.pcap)

**Hint:**

>It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?  
>If you think you found the flag, but it doesn't work, consider that the data may be encrypted.  

## Solution
We open the pcap file with wireshark. By guessing and using the filter `http.request.method == "POST"` we find the following data :  
> userid=stevensj&pswrd=UjZBS05oV3dvNw%3D%3D

The two '%3d' at the end of the the data are '=' sign encoded for url, meaning that the password is probably encoded in base 64. We open our terminal and find:  

    $ echo UjZBS05oV3dvNw== | base64 --decode
	R6AKNhWwo7

Once decoded, the password is `R6AKNhWwo7`.