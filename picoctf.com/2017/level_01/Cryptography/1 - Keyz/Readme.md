# PicoCTF 2017- Level 1 - Cryptography 1

**Title:** Keyz
**Category:** Cryptography
**Points:** 20
**Description:**

>While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com

**Hint:**

>There are plenty of tutorials out there. This one worked for me: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2

## Solution
If you don't have experience with ssh server and public/private key, you can find more information about logging with a private key to a ssh server using putty on [this page](https://system.cs.kuleuven.be/cs/system/security/ssh/setupkeys/putty-with-key.html).

Once log to the webshell, we navigate to the .ssh folder (or create it if it doesn't exist) and add our public key to the authorized_keys file.

	$ cd ~/.ssh
	-bash: cd: /home/aska/.ssh: No such file or directory
	$ mkdir ~/.ssh
	$ echo ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAn5xKYQXvGhRCjsekHjIezd0c4tkiK5iscK8sCHFm/h7DvDOrNtTH4PmCtomyDkyYB/kaXPhhDwQUfVPvnl+FPZbsy0HVh3dmvXlDDXGYEB960hIo8mnJ76o6wxH2+3fHCcgb10PU+20+2BZeZG0/fWqNid9txtwc9Xt2245Rdzf3gFieUSstSd9VHeAy7XIVvznOcjM7yI/Nx+cMep+7euu8yjLeI0o4+ROIO0L9rr/1NVlWOrhIO0OWQ2r6Xb5tx2eLTbWSMUdJleAAYdyJn5MLf7/O2nkAOWp2Rb0N8eouoM1IpIgCW1SqeoNYr2NrA4tmp9pgOxp/gAPzJxjc1Q== rsa-key-20171108 >> authorized_keys

Then we can log from an ssh client:
	$ Authenticating with public key "rsa-key-20171108"
	Congratulations on setting up SSH key authentication!
	Here is your flag: who_needs_pwords_anyways
	
Thus the answer is `who_needs_pwords_anyways`
