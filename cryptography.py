from re import X
import shutil
import os

# reference dictionaries 
alphabet = {0:["a", "A"],1:["b", "B"],2:["c", "C"],3:["d", "D"],4:["e","E"],5:["f","F"],6:["g","G"],7:["h","H"],8:["i","I"],9:["j","J"],10:["k","K"],11:["l","L"],12:["m","M"],
13:["n","N"],14:["o","O"],15:["p","P"],16:["q","Q"],17:["r","R"],18:["s","S"],19:["t","T"],20:["u","U"],21:["v","V"],22:["w","W"],23:["x","X"],24:["y","Y"],25:["z","Z"]}
frequencies = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
english = {820:["a", "A"],150:["b", "B"],280:["c", "C"],430:["d", "D"],1300:["e","E"],220:["f","F"],200:["g","G"],610:["h","H"],700:["i","I"],15:["j","J"],77:["k","K"],400:["l","L"],250:["m","M"],
670:["n","N"],750:["o","O"],190:["p","P"],10:["q","Q"],600:["r","R"],630:["s","S"],910:["t","T"],280:["u","U"],98:["v","V"],240:["w","W"],16:["x","X"],200:["y","Y"],7:["z","Z"]}
simple_e = {0:["e","E"], 1:["t","T"], 2:["a","A"], 3:["o","O"], 4:["i","I"], 5:["n","N"], 6:["s","S"], 7:["h","H"], 8:["r","R"], 9:["d","D"], 10:["l","L"], 11:["c","C"], 12:["u","U"], 13:["m","M"], 
14:["w","W"], 15:["f","F"], 16:["g","G"], 17:["y","Y"], 18:["p","P"], 19:["b","B"], 20:["v","V"], 21:["k","K"], 22:["j","J"], 23:["x","X"], 24:["q","Q"], 25:["z","Z"]}
# global variables
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_list = list(alpha)

# function to encode .txt based on given code
def encoding(code):
    # this encoding method replaces all instances of each letter, within each line break
    with open('copy.txt', 'r') as f:
        for line in f:
            cursor = line
            starting_point = 0
            progress = []
            while len(progress) < (key_limit):
            # establish hold letter (which wants to become 'a')
                x = code[starting_point]
                y = alpha_list.index(x)
                progress.append(starting_point)
                hold_letter = alphabet[y]
            # replace 'a' with placeholder chars
                symbol = alphabet[starting_point]
                cursor = cursor.replace(symbol[0], '@')
                cursor = cursor.replace(symbol[1], '$')

            # first replacement (whichever wants to be 'a')
                new_letter = alphabet[starting_point]
                x = code.index(new_letter[0])
                progress.append(x)
                old_letter = alphabet[x]

                cursor = cursor.replace(old_letter[0], new_letter[0])
                cursor = cursor.replace(old_letter[1], new_letter[1])

            # work backwards through alphabet
                new_letter = old_letter
                while new_letter != hold_letter:
                    x = code.index(new_letter[0])
                    progress.append(x)
                    old_letter = alphabet[x]

                    cursor = cursor.replace(old_letter[0], new_letter[0])
                    cursor = cursor.replace(old_letter[1], new_letter[1])

                    new_letter = old_letter
            
            # replace placeholder chars with hold letter
                cursor = cursor.replace("@", new_letter[0])
                cursor = cursor.replace("$", new_letter[1])
                
            # establish new starting point for first missed letter
                progress.sort()
                num1 = int(0)
                for i in progress:
                    num2 = i
                    if num2 == num1:
                        num1 += 1
                    elif num2 != num1:
                        break
                starting_point = num1

        # write encrypted txt to translation.txt
            translation = open("translation.txt", "a")
            translation.write(cursor)
            translation.close()

##
## to begin, user chooses what the program is going to run ##
##

which_file = input("Which file shall we work with?\n")
copy_file = r'copy.txt'
if not os.path.isfile(which_file):
    print("I can't find that file")
    print("Goodbye")
    quit()
shutil.copyfile(which_file, copy_file)

print("What sort of code are we working with?")
print("1 - shift / Caesar cipher")
print("2 - mixed alphabet cipher")
print("3 - Vigenère cipher")
print("4 - decryption using frequency analysis")
choice = input()

decrypt = False
if choice == "1" or choice == "2" or choice == "3":
    print("What would you like to do?")
    print("1 - Encrypt \n2 - Decrypt")
    question = input()
    if question == "1":
        decrypt = False
    elif question == "2":
        decrypt = True
    else:
        print("I don't understand")
        quit()

# prepare new translation file
if os.path.exists("translation.txt"):
    os.remove("translation.txt")
translation = open("translation.txt", "x")

##
## encoding your .txt using a shift cypher ##
##
if choice == "1":
    print("Please give a shift number, from 1-25.")
    cipher = input()
    if not cipher.isdigit():
        print("That is not a numeric value")
        print("Goodbye")
        quit()
    cipher = int(cipher)
    if cipher < 0 or cipher > 25:
        print("That number is not within the specified range")
        print("Goodbye")
        quit()
    # if decrypting, the shift is inverted
    if decrypt == True:
        cipher = 26-cipher

    # create code alphabet using the shift number
    key = ""
    key_limit = 25
    for char in alpha:
        current_index = alpha_list.index(char)
        target_index = current_index + cipher
        if target_index > 25:
            target_index -= 26
        target_letter = alpha_list[target_index]
        key = key + target_letter
    code = list(key)

    # call encoding function
    encoding(code)

##
## encoding your .txt using a mixed alphabet cipher ##
##
elif choice == "2":
    print("What is your key-phrase?")
    cipher = input()
    if not cipher.isalpha():
        print("Your keyphrase can't contain numbers or symbols")
        quit()

    key = ""
    key_limit = 0
    # remove whitespace
    cipher = cipher.replace(" ", "")
    cipher = cipher.lower()
    for char in cipher:
        # ignoring duplicate letters, construct code for encryption
        if char not in key:
            key = key + char
            # determine latest letter in key, to establish key_limit (letters at the end of the alphabet not encrypted)
            check = alpha_list.index(char)
            if check > key_limit:
                key_limit = check
    # append the rest of the alphabet to the code
    for char in alpha:
        if char not in key:
            key = key + char
    code = list(key)
    # if we're decrypting, have to create the inverse cipher, then pass that through the encryption
    if decrypt == True:
        reverse_code = []
        for char in alpha:
            x = code.index(char)
            y = alpha_list[x]
            reverse_code.append(y)
        code = reverse_code

    # call encoding function
    encoding(code)

##
## encoding your .txt using a Vigenère cipher ##
##
elif choice == "3":
    print("What is your key-phrase?")
    cipher = input()
    if not cipher.isalpha():
        print("Your keyphrase can't contain numbers or symbols")
        quit()

    cipher = cipher.replace(" ", "")
    cipher = cipher.lower()
    length = len(cipher)
    increment = 0
    cipher_list = list(cipher)

    # encoding method swapping each character sequentially
    with open('copy.txt', 'r', encoding='utf-8-sig', errors='ignore') as f:
        for line in f:
            translation = open("translation.txt", "a")
            cursor = ""
            for char in line:
                # ignore punctuation and symbols
                if char.isalpha():
                    char_lo = char.lower()
                    # ignore accented characters
                    if char_lo in alpha_list:
                        # get character index in alphabet
                        x = alpha_list.index(char_lo)
                        # shift the alphabet by that index
                        key = ""
                        for letter in alpha:
                            current_index = alpha_list.index(letter)
                            target_index = current_index + x
                            if target_index > 25:
                                target_index -= 26
                            target_letter = alpha_list[target_index]
                            key = key + target_letter
                        column = list(key)

                        # letter in cipher, taken from incrementing position as index
                        cipher_letter = cipher_list[increment]
                        # alphabet index of letter in cipher, is y position
                        y = alpha_list.index(cipher_letter)
                        # if decrypting, reverse the shift of the row
                        if decrypt: 
                            y = 26 - y
                            if y == 26:
                                y = 0
                        # index in column to get replacement letter
                        new_letter = column[y]

                        # find index of new_letter in alpha_list, then retrieve from alphabet (need upper and lower case) 
                        z = alpha_list.index(new_letter)
                        replacement = alphabet[z]
                        if char.islower():
                            cursor = cursor+replacement[0]
                        elif char.isupper():
                            cursor = cursor+replacement[1]

                        # if at the end of the key-phrase, repeat
                        increment += 1
                        if increment > length-1:
                            increment -= (length)
                else:
                    cursor = cursor+char

        # write encrypted txt to translation.txt               
            translation.write(cursor)
            translation.close()

##
## rough decryption using frequency analysis of .txt ##
##
elif choice == "4":
    # count frequency of each letter
    with open('copy.txt', 'r') as f:
        for line in f:
            for key in alphabet:
                x = alphabet[key]
                lower = x[0]
                upper = x[1]
                count = line.count(lower) + line.count(upper)
                frequencies[lower] += count
    sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    simple_sort = ""
    for item in sorted_items:
        letter = item[0]
        simple_sort=simple_sort+letter
   
    # create cipher based on likely letter-pairs, using frequencies
    key = ""
    key_limit = 25
    for char in alpha:
        where_in_sort = simple_sort.index(char)
        there_in_simple_e = simple_e[where_in_sort]
        new_letter = there_in_simple_e[0]
        key = key + new_letter
    code = list(key)

    # call encoding function
    encoding(code)

else:
    print("I did not understand your selection")
    print("Goodbye")
    quit()

print("Your file should now be translated")
print("Find the file in the directory, it is named translation.txt")
quit()

