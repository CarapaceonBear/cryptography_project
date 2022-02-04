# cryptography_project

Experimenting in python to create a program which can encrypt and decrypt .txt files, using old-school cryptography methods.

-	-	-

Currently run through the console.
The first input is the file name, of a .txt file in the directory.
	The program creates a copy of the original, as well as a translation file.

-	-	-

Encryption options so far:
 - shift / Caesar cipher
	- shifts encoding alphabet by the given number
	- decryption available
 - mixed alphabet cipher
	- jumbles encoding alphabet based on given keyword,
	  then remaining letters are in order
	- decryption available
 - Vigenère cipher
	- cycles through a grid of encoding alphabets, based on given keyword
	- decryption available
 - frequency-analysis based decryption
	- currently very rudimentary

-	-	-

To do list:
 - improve frequency analysis with followup checks
	ie. check double letters, single letter words

-	-	-

Invaluable resource for my cryptography research:
https://crypto.interactive-maths.com/
- also let me check my encoding was working properly
