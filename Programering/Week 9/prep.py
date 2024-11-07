import os





# import os
# cwd = os.getcwd()
# print(cwd)

# import os
# for fi in os.listdir():
#     print(fi)

# import os
# for fi in os.listdir():
#     if os.path.isdir(fi):
#         print(fi, 'is a directory')
#     elif os.path.isfile(fi):
#         print(fi, 'is a file')
#     else:
#         print(fi, 'is not a directory or a file')


# print(os.listdir('Programering/Week 9/week_09_files'))



# import os

# filename = 'Programering/Week 9/week_09_files/mester_jakob.txt'
# test = os.path.isfile(filename)   
# print(test)



# import os

# path = 'Programering/Week 9/week_09_files' # path to the folder containing the file
# filename = os.path.join(path, 'mester_jakob.txt')
# test = os.path.isfile(filename)   
# print(test) 


path = 'Programering/Week 9/week_09_files' # path to the folder containing the file
filename = os.path.join(path, 'mester_jakob.txt')
with open(filename) as file_object:
    content = file_object.read()
print(content)


