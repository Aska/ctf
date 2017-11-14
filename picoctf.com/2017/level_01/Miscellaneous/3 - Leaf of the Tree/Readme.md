# PicoCTF 2017- Level 1 - Miscellaneous 3

**Title:** Leaf of the Tree  
**Category:** Miscellaneous  
**Points:** 20  
**Description:**

>We found this annoyingly named directory tree starting at /problems/8ca1c927e4aedb1db7961d774fa56bcd. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

**Hint:**

>Tab completion is a wonderful, wonderful thing 

## Solution

Let's navigate to the folder and list what's in it:  
	$ cd /problems/8ca1c927e4aedb1db7961d774fa56bcd
	$ ls
	trunk
	$ find . -type f
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/trunk52c5/flag
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/trunk52c5/branch6b9b/leaf1f47
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/trunk52c5/branch6b9b/leaf1858
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/trunk52c5/branch6b9b/leaf44b8
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/branch0b2d/leaf736b
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/branchb1c6/leaf5d39
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/branchb1c6/leaf186e
	./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/branchb1c6/leaf4ae4
	./trunk/trunk9b95/trunkb610/trunkcd2e/branchbbd3/leaff394
	./trunk/trunk9b95/trunkb610/trunkcd2e/branchb18c/leaf22dc
	./trunk/trunk9b95/branche68e/leafc2a6
	./trunk/trunk9b95/branche68e/leaf8863
	./trunk/trunk9b95/branche68e/leaf8925
	./trunk/trunk9b95/branch336c/leafd5da
	$ cat ./trunk/trunk9b95/trunkb610/trunkcd2e/trunk2498/trunk24e1/trunk1d04/trunk52c5/flag
	d0bc754c90a5514b4d10d2f038eba8df

The solution is `d0bc754c90a5514b4d10d2f038eba8df`