# PicoCTF 2017- Level 2 - Forensics 3

**Title:** Just Keyp Trying  
**Category:** Forensics  
**Points:** 80  
**Description:**

>Here's an interesting capture of some data. But what exactly is this data? Take a look: [data.pcap](data.pcap)

**Hint:**

>Find out what kind of packets these are. What does the info column say in Wireshark/Cloudshark?  
>What changes between packets? What does that data look like?  
>Maybe take a look at http://www.usb.org/developers/hidpage/Hut1_12v2.pdf?  

## Solution

Checking the [data.pcap](data.pcap) file we can see that one of the only thing changing in each packet are the "Leftover Capture Data". Using the command:  
>tshark -r data.pcap -T fields -e usb.capdata > output.txt  

We get a text file containing the following lines:  
>00:00:09:00:00:00:00:00  
>00:00:00:00:00:00:00:00  
>00:00:0f:00:00:00:00:00  
>00:00:00:00:00:00:00:00  
>00:00:04:00:00:00:00:00  
>00:00:00:00:00:00:00:00  
>00:00:0a:00:00:00:00:00  
>00:00:00:00:00:00:00:00  
>20:00:00:00:00:00:00:00  
>20:00:2f:00:00:00:00:00  
>...  

We can see than only the values in the second column are changing. Once isolated, we get:  
>09 00 0f 00 04 00 0a 00 00 2f 00 00 13 00 15 00 20 00 22 00 22 00 00 2d 00 00 27 00 11 00 1a 00 04 00 15 00 07 00 16 00 00 2d 00 00 06 00 26 00 25 00 06 00 06 00 09 00 26 00 26 00 00 30 00 00 00 06  

Those bytes cannot be transformed from hex to ascii but by taking a look at the clue and the title of the challenge, we find a table to convert hex input from keyboard to characters (page 53 to 59 of the pdf). We get:  
>f l a g { p r 3 5 5 _ 0 n w a r d s _ c 9 8 c c f 9 9 } c  

Thus the answer is `pr355_0nwards_c98ccf99`  