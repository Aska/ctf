# PicoCTF 2017- Level 1 - Master Challenge

**Title:** Lazy Dev  
**Category:** Master Challenge  
**Points:** 50  
**Description:**

>I really need to login to this [website](http://shell2017.picoctf.com:4370/), but the developer hasn't implemented login yet. Can you help?  

**Hint:**

>Where does the password check actually occur?  
>Can you interact with the javascript directly?  

## Solution

By looking at the page's source code, we can see that the identification use javascript. By changing:  
```javascript
function validate(pword){
	//TODO: Implement me
	return false;
}
```
To:
```javascript
function validate(pword){
	//TODO: Implement me
	return pword;
}
```
And then sending the form with any password, the page answer :
	client_side_is_the_dark_side0c97381c155aae62b9ce3c59845d6941

Thus, the solution to the master challenge is `client_side_is_the_dark_side0c97381c155aae62b9ce3c59845d6941`