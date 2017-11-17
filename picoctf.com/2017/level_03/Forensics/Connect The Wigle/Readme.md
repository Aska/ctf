# PicoCTF 2017- Level 3 - Forensics

**Title:** Connect The Wigle  
**Category:** Forensics  
**Points:** 140  
**Description:**

>Identify the data contained within [wigle](wigle) and determine how to visualize it. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out.  

**Hint:**

>Perhaps they've been storing data in a database. How do we access the information?  
>How can we visualize this data? Maybe we just need to take a step back to get the big picture?  
>Try zero in the first word of the flag, if you think it's an O.  
>If you think you're super close, make a private piazza post with what you think it is.  

## Solution

After giving a quick glance a the `wigle` file, we can see that it is a `SQLite` database. After reopenning it in a database browser, we can notice that it contains a list of locations, probably drawing the flag on map.  
If we only keep the [coordinates](coords.txt) and use a website like [this one](https://www.darrinward.com/lat-long/?id=5a0eed3ae35992.77669407) to represent them all on a map at the same time, we can read:  
>flag{f0und_m3_33de7930}  


The flag for this problem is `flag{f0und_m3_33de7930}`