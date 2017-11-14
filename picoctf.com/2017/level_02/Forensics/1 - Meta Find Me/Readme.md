# PicoCTF 2017- Level 2 - Forensics 1

**Title:** Meta Find Me  
**Category:** Forensics  
**Points:** 70  
**Description:**

>Find the location of the flag in the image: [image.jpg](image.jpg). Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

**Hint:**

>How can images store location data? Perhaps search for GPS info on photos.

## Solution

For this one we just need to look at the exif of the photo. A website like [verexif.com](https://www.verexif.com/en/ver.php) will do.

>Date/Time :  
>    2016/02/10 11:55:56  
>Resolution :    500 x 500  
>Jpeg process :    Progressive  
>GPS Latitude :    ? 7º 0' 0"  
>GPS Longitude :    ? 96º 0' 0"  
>Comment :    "Your flag is flag_2_meta_4_me_<lat>_<lon>_1c1f. Now find the GPS coordinates of this image! (Degrees only please)"  

Thus the answer is `flag_2_meta_4_me_7_96_1c1f`