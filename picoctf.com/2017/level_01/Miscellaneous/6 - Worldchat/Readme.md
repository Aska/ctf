# PicoCTF 2017- Level 1 - Miscellaneous 6

**Title:** Worldchat  
**Category:** Miscellaneous  
**Points:** 30  
**Description:**

>We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:11511. Remember to use Ctrl-C to cut the connection if it overwhelms you!  

**Hint:**

>There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)  

## Solution

Let's connect to the server and grep the answers:  
	$ nc shell2017.picoctf.com 11511 | grep "flag"

	10:40:10 ihazflag: your dad has attacked my toes to understand me
	10:40:10 whatisflag: your dad will never understand me to help me spell 'raspber
	ry' correctly
	10:40:11 personwithflag: that guy from that movie would like to meet you to make
	 a rasberry pie
	10:40:11 whatisflag: My friend would like to meet you to make a rasberry pie
	10:40:11 ihazflag: Several heavily mustached dolphins need to meet up for what,
	I do not know
	10:40:12 ihazflag: Scary pandas give me hope for what, I do not know
	10:40:12 whatisflag: A huge moose has attacked my toes to make a rasberry pie
	10:40:12 whatisflag: Anyone but me wants to see me to create a self driving car
	10:40:12 noihazflag: Several heavily mustached dolphins will never be able to cr
	eate a self driving car
	10:40:13 noihazflag: your dad will never understand me to generate fusion power
	10:40:13 whatisflag: my homie wants to see me to generate fusion power
	10:40:13 whatisflag: A huge moose wants to see me to drink your milkshake
	10:40:14 flagperson: this is part 1/8 of the flag - 8d84
	ng car

As we can see in the last line, the flag is probably divided in different parts that are posted from time to time in the chat. So let's search for: "/8 of the flag"  

	$ nc shell2017.picoctf.com 11511 | grep "/8 of the flag"

	10:43:35 flagperson: this is part 1/8 of the flag - 8d84
	10:43:41 flagperson: this is part 2/8 of the flag - 913f
	10:43:41 flagperson: this is part 3/8 of the flag - 84bd
	10:43:43 flagperson: this is part 4/8 of the flag - 68a4
	10:43:43 flagperson: this is part 5/8 of the flag - 6576
	10:43:45 flagperson: this is part 6/8 of the flag - 3e48
	10:43:45 flagperson: this is part 7/8 of the flag - d9d9
	10:43:46 flagperson: this is part 8/8 of the flag - ca1c

Once all parts of the flag are concatenated, the solution is `8d84913f84bd68a465763e48d9d9ca1c`