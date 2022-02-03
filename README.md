# cryptography_project

Experimenting in python to create a program which can encrypt and decrypt txt files

Currently run through terminal.
First input is the file name, of a .txt file in the directory
	Creates a copy of the original, as well as a translation file

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
 - frequency-analysis based decryption
	- currently very rudimentary


To do list:
 - improve frequency analysis with followup checks
	ie. check double letters, single letter words
 - decrypt vigeneres cipher? Not researched how hard that is