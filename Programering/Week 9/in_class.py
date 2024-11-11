import os
fil="efternavne.csv"
path='Programering/Week 9/week_09_files'
filename=os.path.join(path, fil)



# #Opgave 9.2
# with open(filename) as file_object:
#     content=file_object.read()

# # content=content.lower()
# a="a"
# b="A"
# count=0
# print(count)
# for char in content:
#     if char==a:
#         count=count+1

# print(f"Små bogstaver: {count}")

# count=0
# print(count)
# for char in content:
#     if char==b:
#         count=count+1
# print(f"Store bogstaver: {count}")

#Opgave 9.3


# def count_letter(text, letter):
#     filename=os.path.join(path, text)
#     with open(filename) as file_object:
#         content=file_object.read()
#     content=content.lower()

#     a=letter
#     count=0
#     for char in content:
#         if char==a:
#             count=count+1
#     return count

# print(count_letter("alice_large.txt", "a"))




# #Opgave 9.4
# letters="abcdefghijklmnopqrstuvwxyz"
# letters=letters+letters.upper()
# letter_count={}
# print(letters)

# for letter in letters:
#     letter_count[letter]=0


# with open(filename) as file_object:
#     content=file_object.read()

# for char in content:
#     if char in letters:
#         letter_count[char]=letter_count[char]+1


# print(letter_count)


# #Opgave 9.5

# def count_letters(fil):
#     filename=os.path.join(path, fil)
#     letters="abcdefghijklmnopqrstuvwxyz"
#     letter_count={}

#     for letter in letters:
#         letter_count[letter]=0


#     with open(filename) as file_object:
#         content=file_object.read()

#     for char in content:
#         if char in letters:
#             letter_count[char]=letter_count[char]+1
#     return letter_count


# print(count_letters("quick_fox.txt"))



#Opgave 9.6

with open(filename) as f:
    content = f.read()
content = content.splitlines()

count=0
for item in content:
    i = item.split(",")
    count=count+int(i[1])

print(count)



# print(count)
# for tal in delt[1:]:
#     count=count+int(tal)

# print(count)

