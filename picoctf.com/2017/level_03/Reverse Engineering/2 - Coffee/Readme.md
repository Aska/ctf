# PicoCTF 2017- Level 3 - Reverse Engineering 2

**Title:** Coffee  
**Category:** Reverse Engineering  
**Points:** 115  
**Description:**

>You found a suspicious USB drive in a jar of pickles. It contains this [file](freeThePickles.class).  

**Hint:**

>Is there a way to get the source of the program?  

## Solution

By openning this file we can see that it is a `java` class. First, let's use [this website](http://www.javadecompilers.com) to decompile it to the following code:  
```java
import java.util.Base64.Decoder;

public class problem {
  public problem() {}
  
  public static String get_flag() { String str1 = "Hint: Don't worry about the schematics";
    String str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
    String str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
    byte[] arrayOfByte1 = str2.getBytes();
    byte[] arrayOfByte2 = str3.getBytes();
    byte[] arrayOfByte3 = new byte[arrayOfByte2.length];
    for (int i = 0; i < arrayOfByte2.length; i++)
    {
      arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    }
    System.out.println(java.util.Arrays.toString(java.util.Base64.getDecoder().decode(arrayOfByte3)));
    return new String(java.util.Base64.getDecoder().decode(arrayOfByte3));
  }
  
  public static void main(String[] paramArrayOfString) {
    System.out.println("Nothing to see here");
  }
}
```

As we can see this is a simple program, let's replicate it in python:
```python
import base64

list_one = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd".encode()
list_two = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc".encode()
list_three = []

for i in range(len(list_one)):
	list_three.append(list_two[list_one[i] - 90])

string = bytearray(list_three).decode()
print("The flag is:", base64.b64decode(string).decode())
```

Thus the flag is `flag_{pretty_cool_huh}`