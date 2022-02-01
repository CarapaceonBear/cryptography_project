import shutil
import os


question = input("Which file shall we work with? ")
#os.path.isfile(question)
target = r'copy.txt'
shutil.copyfile(question, target)


decrypt = False
question = input("Would you like to encrypt or decrypt your file? ")
if question == "encrypt":
    pass
elif question == "decrypt":
    decrypt = True
else:
    print("I don't understand")
    quit()

##
## encoding your .txt using a shift cypher ##
##

cypher = int(input("Please give a shift number, from 1-25. "))
if cypher < 0 or cypher > 25:
    print("I can't shift that much!")
    print("I'll give you one more try:")
    temp = int(input("Please give a shift number, from 1-25. "))
    cypher = temp
if decrypt == True:
   cypher = 26-cypher

#caesar = len(cypher)
# alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
# shift = []
# n = 0
# for value in alphabet.values():
#     value += cypher
#     if value > 25:
#         value -= 26
#     shift.append(value)
#     n += 1

alphabet = {0:["a", "A"],1:["b", "B"],2:["c", "C"],3:["d", "D"],4:["e","E"],5:["f","F"],6:["g","G"],7:["h","H"],8:["i","I"],9:["j","J"],10:["k","K"],11:["l","L"],12:["m","M"],
13:["n","N"],14:["o","O"],15:["p","P"],16:["q","Q"],17:["r","R"],18:["s","S"],19:["t","T"],20:["u","U"],21:["v","V"],22:["w","W"],23:["x","X"],24:["y","Y"],25:["z","Z"]}

if os.path.exists("translation.txt"):
    os.remove("translation.txt")
translation = open("translation.txt", "x")

odd = False
iteration_limit = 10
if cypher % 2 != 0:
    odd = True
    iteration_limit = 23

with open('copy.txt', 'r') as f:
    for line in f:
        cursor = line

# first letter change, target held as temporary characters
        target = alphabet[cypher]
        cursor = cursor.replace(target[0], '@')
        cursor = cursor.replace(target[1], '$')
        old_letter = alphabet[0]
        new_letter = target
        cursor = cursor.replace(old_letter[0], new_letter[0])
        cursor = cursor.replace(old_letter[1], new_letter[1])

# last in sequence replacing first in sequence
        increment = 26
        old_letter = alphabet[(increment-cypher)]
        new_letter = alphabet[0]
        cursor = cursor.replace(old_letter[0], new_letter[0])
        cursor = cursor.replace(old_letter[1], new_letter[1])
        increment -= cypher

# iterate backwards through the shifted alphabet
        iterations = 0
        while iterations < iteration_limit:
            reverse = increment-cypher
            if reverse < 0:
                reverse += 26
            old_letter = alphabet[(reverse)]
            new_letter = alphabet[increment]
            cursor = cursor.replace(old_letter[0], new_letter[0])
            cursor = cursor.replace(old_letter[1], new_letter[1])
            increment -= cypher
            if increment < 0:
                increment += 26
            iterations += 1

# final change, replacing temporary characters
        new_letter = alphabet[increment]
        cursor = cursor.replace('@', new_letter[0])
        cursor = cursor.replace('$', new_letter[1])

    # additional cycle if cypher is even
        if not odd:
            target = alphabet[cypher+1]
            cursor = cursor.replace(target[0], '@')
            cursor = cursor.replace(target[1], '$')
            old_letter = alphabet[1]
            new_letter = target
            cursor = cursor.replace(old_letter[0], new_letter[0])
            cursor = cursor.replace(old_letter[1], new_letter[1])

            increment = 27
            old_letter = alphabet[(increment-cypher)]
            new_letter = alphabet[1]
            cursor = cursor.replace(old_letter[0], new_letter[0])
            cursor = cursor.replace(old_letter[1], new_letter[1])
            increment -= cypher

            iterations = 0
            while iterations < iteration_limit:
                reverse = increment-cypher
                if reverse < 0:
                    reverse += 26
                old_letter = alphabet[(reverse)]
                new_letter = alphabet[increment]
                cursor = cursor.replace(old_letter[0], new_letter[0])
                cursor = cursor.replace(old_letter[1], new_letter[1])
                increment -= cypher
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
## frequency analysis of text ##
##

# frequencies = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
# with open('copy.txt') as f:
#     for line in f:
#         temp = line.count("A") + line.count("a")
#         frequencies["a"] += temp
#         temp = line.count("B") + line.count("b")
#         frequencies["b"] += temp
#         temp = line.count("C") + line.count("c")
#         frequencies["c"] += temp
#         temp = line.count("D") + line.count("d")
#         frequencies["d"] += temp
#         temp = line.count("E") + line.count("e")
#         frequencies["e"] += temp
#         temp = line.count("F") + line.count("f")
#         frequencies["f"] += temp
#         temp = line.count("G") + line.count("g")
#         frequencies["g"] += temp
#         temp = line.count("H") + line.count("h")
#         frequencies["h"] += temp
#         temp = line.count("I") + line.count("i")
#         frequencies["i"] += temp
#         temp = line.count("J") + line.count("j")
#         frequencies["j"] += temp
#         temp = line.count("K") + line.count("k")
#         frequencies["k"] += temp
#         temp = line.count("L") + line.count("l")
#         frequencies["l"] += temp
#         temp = line.count("M") + line.count("m")
#         frequencies["m"] += temp
#         temp = line.count("N") + line.count("n")
#         frequencies["n"] += temp
#         temp = line.count("O") + line.count("o")
#         frequencies["o"] += temp
#         temp = line.count("P") + line.count("p")
#         frequencies["p"] += temp
#         temp = line.count("Q") + line.count("q")
#         frequencies["q"] += temp
#         temp = line.count("R") + line.count("r")
#         frequencies["r"] += temp
#         temp = line.count("S") + line.count("s")
#         frequencies["s"] += temp
#         temp = line.count("T") + line.count("t")
#         frequencies["t"] += temp
#         temp = line.count("U") + line.count("u")
#         frequencies["u"] += temp
#         temp = line.count("V") + line.count("v")
#         frequencies["v"] += temp
#         temp = line.count("W") + line.count("w")
#         frequencies["w"] += temp
#         temp = line.count("X") + line.count("x")
#         frequencies["x"] += temp
#         temp = line.count("Y") + line.count("y")
#         frequencies["y"] += temp
#         temp = line.count("Z") + line.count("z")
#         frequencies["z"] += temp
# first = frequencies["a"]
# second = frequencies["b"]
# third = frequencies["m"]
# fourth = frequencies["z"]
# print(f"a = {first}")
# print(f"b = {second}")
# print(f"m = {third}")
# print(f"z = {fourth}")

