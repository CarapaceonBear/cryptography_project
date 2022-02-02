import shutil
import os


question = input("Which file shall we work with?\n")
#os.path.isfile(question)
target = r'copy.txt'
shutil.copyfile(question, target)

print("What sort of code are we working with?")
print("1 - shift / Caesar cipher\n 2 - mixed alphaber cipher\n 3 - we'll see")
choice = int(input())

decrypt = False
question = input("Would you like to encrypt or decrypt your file? \n")
if question == "encrypt" or "e":
    pass
elif question == "decrypt" or "d":
    decrypt = True
else:
    print("I don't understand")
    quit()

alphabet = {0:["a", "A"],1:["b", "B"],2:["c", "C"],3:["d", "D"],4:["e","E"],5:["f","F"],6:["g","G"],7:["h","H"],8:["i","I"],9:["j","J"],10:["k","K"],11:["l","L"],12:["m","M"],
13:["n","N"],14:["o","O"],15:["p","P"],16:["q","Q"],17:["r","R"],18:["s","S"],19:["t","T"],20:["u","U"],21:["v","V"],22:["w","W"],23:["x","X"],24:["y","Y"],25:["z","Z"]}
frequencies = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
english = {820:["a", "A"],150:["b", "B"],280:["c", "C"],430:["d", "D"],1300:["e","E"],220:["f","F"],200:["g","G"],610:["h","H"],700:["i","I"],15:["j","J"],77:["k","K"],400:["l","L"],250:["m","M"],
670:["n","N"],750:["o","O"],190:["p","P"],10:["q","Q"],600:["r","R"],630:["s","S"],910:["t","T"],280:["u","U"],98:["v","V"],240:["w","W"],16:["x","X"],200:["y","Y"],7:["z","Z"]}
simple_e = {0:["e","E"], 1:["t","T"], 2:["a","A"], 3:["o","O"], 4:["i","I"], 5:["n","N"], 6:["s","S"], 7:["h","H"], 8:["r","R"], 9:["d","D"], 10:["l","L"], 11:["c","C"], 12:["u","U"], 13:["m","M"], 
14:["w","W"], 15:["f","F"], 16:["g","G"], 17:["y","Y"], 18:["p","P"], 19:["b","B"], 20:["v","V"], 21:["k","K"], 22:["j","J"], 23:["x","X"], 24:["q","Q"], 25:["z","Z"]}

if os.path.exists("translation.txt"):
    os.remove("translation.txt")
translation = open("translation.txt", "x")

##
## encoding your .txt using a shift cypher ##
##
if choice == 1:
    cipher = int(input("Please give a shift number, from 1-25. \n"))
    if cipher < 0 or cipher > 25:
        print("I can't shift that much!")
        print("I'll give you one more try:")
        temp = int(input("Please give a shift number, from 1-25. \n"))
        cipher = temp
    if decrypt == True:
        cipher = 26-cipher

    odd = False
    iteration_limit = 10
    if cipher % 2 != 0:
        odd = True
        iteration_limit = 23

    with open('copy.txt', 'r') as f:
        for line in f:
            cursor = line

    # first letter change, target held as temporary characters
            target = alphabet[cipher]
            cursor = cursor.replace(target[0], '@')
            cursor = cursor.replace(target[1], '$')
            old_letter = alphabet[0]
            new_letter = target
            cursor = cursor.replace(old_letter[0], new_letter[0])
            cursor = cursor.replace(old_letter[1], new_letter[1])

    # last in sequence replacing first in sequence
            increment = 26
            old_letter = alphabet[(increment-cipher)]
            new_letter = alphabet[0]
            cursor = cursor.replace(old_letter[0], new_letter[0])
            cursor = cursor.replace(old_letter[1], new_letter[1])
            increment -= cipher

    # iterate backwards through the shifted alphabet
            iterations = 0
            while iterations < iteration_limit:
                reverse = increment-cipher
                if reverse < 0:
                    reverse += 26
                old_letter = alphabet[(reverse)]
                new_letter = alphabet[increment]
                cursor = cursor.replace(old_letter[0], new_letter[0])
                cursor = cursor.replace(old_letter[1], new_letter[1])
                increment -= cipher
                if increment < 0:
                    increment += 26
                iterations += 1

    # final change, replacing temporary characters
            new_letter = alphabet[increment]
            cursor = cursor.replace('@', new_letter[0])
            cursor = cursor.replace('$', new_letter[1])

        # additional cycle if cypher is even
            if not odd:
                target = alphabet[cipher+1]
                cursor = cursor.replace(target[0], '@')
                cursor = cursor.replace(target[1], '$')
                old_letter = alphabet[1]
                new_letter = target
                cursor = cursor.replace(old_letter[0], new_letter[0])
                cursor = cursor.replace(old_letter[1], new_letter[1])

                increment = 27
                old_letter = alphabet[(increment-cipher)]
                new_letter = alphabet[1]
                cursor = cursor.replace(old_letter[0], new_letter[0])
                cursor = cursor.replace(old_letter[1], new_letter[1])
                increment -= cipher

                iterations = 0
                while iterations < iteration_limit:
                    reverse = increment-cipher
                    if reverse < 0:
                        reverse += 26
                    old_letter = alphabet[(reverse)]
                    new_letter = alphabet[increment]
                    cursor = cursor.replace(old_letter[0], new_letter[0])
                    cursor = cursor.replace(old_letter[1], new_letter[1])
                    increment -= cipher
                    if increment < 0:
                        increment += 26
                    iterations += 1
                
                new_letter = alphabet[increment]
                cursor = cursor.replace('@', new_letter[0])
                cursor = cursor.replace('$', new_letter[1])

    # write encrypted txt to translation.txt
            translation = open("translation.txt", "a")
            translation.write(cursor)
            translation.close()

##
## encoding your .txt using a mixed alphabet cipher ##
##
elif choice == 2:
    cipher = input("What is your key-phrase? \n")
    # remove whitespace, remove duplicate letters, then append the rest of the alphabet, then convert into a list, to search for index during translation 
    # also determine latest letter in key, to find how many letters at the end of the alphabet aren't affected
    key = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_list = list(alpha)
    key_limit = 0
    cipher = cipher.replace(" ", "")
    for char in cipher:
        if char not in key:
            key=key+char
            check = alpha_list.index(char)
            if check > key_limit:
                key_limit = check
    for char in alpha:
        if char not in key:
            key=key+char
    code = list(key)

    with open('copy.txt', 'r') as f:
        for line in f:
            cursor = line
            starting_point = 0
            progress = []

            while len(progress) < (key_limit):
            # establish hold letter (which wants to become 'a')
                temp = code[starting_point]
                temp2 = alpha_list.index(temp)
                progress.append(starting_point)
                hold_letter = alphabet[temp2]
            # replace 'a' with placeholder chars
                symbol = alphabet[starting_point]
                cursor = cursor.replace(symbol[0], '@')
                cursor = cursor.replace(symbol[1], '$')

            # first replacement (whichever wants to be 'a')
                new_letter = alphabet[starting_point]
                temp = code.index(new_letter[0])
                progress.append(temp)
                old_letter = alphabet[temp]

                cursor = cursor.replace(old_letter[0], new_letter[0])
                cursor = cursor.replace(old_letter[1], new_letter[1])

            # work backwards through alphabet
                new_letter = old_letter
                while new_letter != hold_letter:
                    temp = code.index(new_letter[0])
                    progress.append(temp)
                    old_letter = alphabet[temp]

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
## frequency analysis of text ##
##
elif choice == 3:
    with open('copy.txt') as f:
        for line in f:
            temp = line.count("A") + line.count("a")
            frequencies["a"] += temp
            temp = line.count("B") + line.count("b")
            frequencies["b"] += temp
            temp = line.count("C") + line.count("c")
            frequencies["c"] += temp
            temp = line.count("D") + line.count("d")
            frequencies["d"] += temp
            temp = line.count("E") + line.count("e")
            frequencies["e"] += temp
            temp = line.count("F") + line.count("f")
            frequencies["f"] += temp
            temp = line.count("G") + line.count("g")
            frequencies["g"] += temp
            temp = line.count("H") + line.count("h")
            frequencies["h"] += temp
            temp = line.count("I") + line.count("i")
            frequencies["i"] += temp
            temp = line.count("J") + line.count("j")
            frequencies["j"] += temp
            temp = line.count("K") + line.count("k")
            frequencies["k"] += temp
            temp = line.count("L") + line.count("l")
            frequencies["l"] += temp
            temp = line.count("M") + line.count("m")
            frequencies["m"] += temp
            temp = line.count("N") + line.count("n")
            frequencies["n"] += temp
            temp = line.count("O") + line.count("o")
            frequencies["o"] += temp
            temp = line.count("P") + line.count("p")
            frequencies["p"] += temp
            temp = line.count("Q") + line.count("q")
            frequencies["q"] += temp
            temp = line.count("R") + line.count("r")
            frequencies["r"] += temp
            temp = line.count("S") + line.count("s")
            frequencies["s"] += temp
            temp = line.count("T") + line.count("t")
            frequencies["t"] += temp
            temp = line.count("U") + line.count("u")
            frequencies["u"] += temp
            temp = line.count("V") + line.count("v")
            frequencies["v"] += temp
            temp = line.count("W") + line.count("w")
            frequencies["w"] += temp
            temp = line.count("X") + line.count("x")
            frequencies["x"] += temp
            temp = line.count("Y") + line.count("y")
            frequencies["y"] += temp
            temp = line.count("Z") + line.count("z")
            frequencies["z"] += temp

    sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    print(sorted_items)

    with open('copy.txt', 'r') as f:
        for line in f:
            cursor = line
            #for letter in sorted_items():
            # this has become a list, so won't work like this
            pass
    pass

