# PicoCTF 2017- Level 1 - Forensics 2

**Title:** Digital Camouflage  
**Category:** Forensics  
**Points:** 50  
**Description:**

>We can get into the Administrator's computer with a browser exploit. But first, we need to figure out what browser they're using. Perhaps this information is located in a network packet capture we took: [data.pcap](data.pcap). Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)

**Hint:**

>It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?  
>Where can we find information on the browser in networking data? Maybe try reading up on user-agent strings.  

## Solution
By simply searching the string `user-agent` on wireshark we find:  
> User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36\r\n

Following the level explanations, the answer is `Chrome 36.0.1985`