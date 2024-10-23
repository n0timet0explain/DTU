##7.2
# bm_string = "batmand"
# print(bm_string[0])
# print(bm_string[3])
# print(bm_string[0:3])
# print(bm_string[3:])
# print(bm_string[::2])
# print(bm_string[::-1])
# print(bm_string[-1::-2])


# my_string = "I am a student at DTU"
# my_character = my_string[0]
# my_substring = my_string[6:14]

# check = my_character + my_substring
# print(check)


# ##7.3
# # my_string = "i am a student at DTU."
# # my_string[0] = "I"
# # print(my_string)

# my_string = "i am a student at DTU."
# my_string = "I" + my_string[1:]
# print(my_string)


# ##7.4

# my_string = 'Engineering is fun!'
# for i in range(len(my_string)):
#     print('Character with index', i, 'is', my_string[i])

# for char in "Engineering is fun!":
#     print(char)


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiou"
# consonants = ""
# for char in alphabet:
#     if char not in vowels:
#         consonants = consonants + char
# print(consonants)


##7.5
# # # # title = "02002 Computer Programming"
# # # # print(title)
# # # # title = title.upper()
# # # # print(title)
# # # # title = title.lower()
# # # # print(title)


# # # my_string = "Mississippi River is a river in the United States."

# # # count1 = my_string.count("s")
# # # count2 = my_string.count("S")
# # # count3 = my_string.count("i")
# # # count4 = my_string.count("x")
# # # count5 = my_string.count("iss")

# # # print(count1, count2, count3, count4, count5)

# # my_string = "One two three four five six seven eight nine ten"

# # index1 = my_string.index("e")
# # index2 = my_string.index("two")
# # index3 = my_string.index("ten")
# # print(index1, index2, index3)

# # index4 = my_string.index("f")
# # index5 = my_string.index("f", index4 + 1)
# # # index6 = my_string.index("f", index5 + 1)

# # print(index4, index5,)

# # index7 = my_string.index("g")
# # # index8 = my_string.index("g", 0, 30)
# # print(index7)


# s = "Zinc is a metal"
# s = s.replace("Zinc", "Iron")
# print(s)

##7.6
# # # # physicists_string = "Bohr Heisenberg Schrödinger Dirac Pauli Fermi"
# # # # physicists = physicists_string.split()
# # # # print(physicists)


# # # spaces_string = "many   spaces"
# # # print("1")
# # # print(spaces_string.split())
# # # print("2")
# # # print(spaces_string.split(" "))

# # # ratings = "Great, Good, Poor, Okay, Poor, Good, Great, Okay"
# # # print("3")
# # # print(ratings.split(", "))

# # # question = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
# # # print("4")
# # # print(question.split("chuck"))
# # # print("5")
# # # print(question.split("wood"))


# # physicists = ['Bohr', 'Heisenberg', 'Schrödinger', 'Dirac', 'Pauli', 'Fermi']
# # separator = " "
# # together = separator.join(physicists)
# # print(together)

# physicists = ['Bohr', 'Heisenberg', 'Schrödinger', 'Dirac', 'Pauli', 'Fermi']
# joint = ", ".join(physicists)
# print(joint)
# print(" - . - ".join(physicists))


##7.7
# # dna_seq = 'TTAACGCATGCCATAGGACGGTTAGGCTCAGAACCCGCAACCAATACACGTGATTTTCTCGTCCCCTG'
# # pattern = 'CTCG'
# # match = pattern in dna_seq
# # print(match)

# print("i" in "Mississippi")
# print("I" in "Mississippi")
# print("kansas" in "arkansas")
# print("Kansas" in "arkansas")


##7.8
# # # # # planet = 'Mars'
# # # # # distance = 1.5
# # # # # message = f"{planet} is {distance} AU from the Sun"
# # # # # print(message)

# # # # for name in ["Anders", "Vedrana"]:
# # # #     if name=="Vedrana":
# # # #         s = "is"  
# # # #     else:
# # # #         s = "is NOT"
# # # #     print(f"{name} {s} teaching this course.")


# # # import math
# # # print(f"Pi to 3 decimal places is {math.pi:.3f}")
# # # print(f"Two thirds is {2/3}")
# # # print(f"Two thirds with 5 decimal places is {2/3:.5f}")


# # for i in range(1, 11):
# #     s = ""
# #     for j in range(1, 11):
# #         s = s + f'{i*j:4}' 
# #     print(s)    


# hours = 9
# minutes = 5
# print(f"Time is {hours:02}:{minutes:02}")


# def greatest_common_divisor(a, b):
#     divisor = 1
#     for i in range(2, min(a, b)+1):
#         if a % i == 0 and b % i == 0:
#             divisor = i
#     return divisor

# a = 12
# b = 18
# gcd = greatest_common_divisor(a, b)
# print(f"Simplifying ratio {a}/{b}:\n {a}/{b} = ({a}/{gcd})/({b}/{gcd}) = {a//gcd}/{b//gcd} = {a/b:.3f}")

# max_iter = 1000
# pi = 0
# for i in range(1, max_iter+1):
#     pi = pi + 4 * (-1)**(i+1) / (2*i-1)
#     if i % 100 == 0 or i in [1, 10, 20, 50]:
#         print(f"Approximating pi step {i:04}/{max_iter}: {pi:.5f}")


##7.9
# my_string = "This is the first line.\nThis is the second line."
# print(my_string)

# message = "Hello" + 12*"\n-" + "\nWorld"
# print(message)

# print(len(message))


# print("One\ttwo\tthree\tfour")
# print("En\tto\ttre\tfire")

# print("C:\\Users\\username\\Documents\\file.txt")

# text = "First line\nSecond line\nThird line"
# lines = text.split('\n')
# print(lines)




##7.10
# print("dtu".upper())

# import math
# print(f"The value of pi is {math.pi:.5f}")

# last_name = "Hannemose"
# print("The last letter of my last name is", last_name[-1])

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print("first letter of the alphabet:", alphabet[0])

# path = "C:\\Documents\\User\\File"
# print(path)

# print(f"pi repeated 5 times (for fun): {'3.14 '*5}")
# print(f"e repeated 5 times (for fun): {'2.71 ' *5}")



print("i'm not angry!".upper())

lyrics = "Looks like it's gonna be a great day today"
print(lyrics.split()[6])

print("I am a string".replace("a", "another"))

stans = "kazakhstan, uzbekistan, stanistan, turkmenistan"
print(stans.replace("stan", "land").split(", "))

print(("O"*20+"\n")*10)

print(f"{2002} Computer Programming")
print(f"{2002:5d} Computer Programming")
print(f"{2002:05d} Computer Programming")

fum = 5
bum = 7
print(f"{fum}+{bum}={fum+bum}")