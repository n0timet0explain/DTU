import os
path = 'Programering/Week 9/' # path to the folder containing the file




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



filename = os.path.join(path, 'mester_jakob.txt')
with open(filename) as file_object:
    content = file_object.read()


# ########## Alt metode til at åbne filer
# # file_object = open(filename)
# # content = file_object.read()
# # file_object.close()


# # for i in range(len(content)):
# #     print(i, content[i])

print(repr(content[26]))
print(repr(content))

# lines = content.splitlines()
# print(lines)

# print(type(lines))

# print(len(lines))
# for line in lines: print(line)



# filename = os.path.join(path, 'week_09_files/mester_jakob.txt')
# with open(filename) as f:
#     lines = f.readlines()
# print(lines)

# print(type(lines))
# print(len(lines))
# for line in lines: print(line)

# for line in lines:
#     print(line.strip()) 







# filename = os.path.join(path, 'hamlet.txt')
# with open(filename) as f:
#     content = f.read()
# print(len(content))
# print(type(content))
# print(content)

# lines = content.splitlines()
# print(len(lines))
# print(type(lines))
# for line in lines: print(line)

filename=os.path.join(path, "my_testing_place.txt")
with open(filename, 'w') as f:
    for i in range(3):
        f.write( 12 * '-~' + '\n')
        f.write(5 * ' ' + 'Just testing!\n')
        f.write( 12 * '-~' + 4 *'\n')


# with open(filename, 'w') as f:
#     content = f.read()
#     print(content)






# test=['Just testing!', 'Another test!', 'Yet another test!']

# filename_in = os.path.join(path, "week_09_files/mester_jakob.txt")
# filename_out = os.path.join(path, "mester_jakob_out.txt")

# with open(filename_in) as file_in:
#     lines = file_in.readlines()

# for i in range(len(lines)):
#     lines[i] = f'Line {i:02}: ' + lines[i]

# with open(filename_out, 'w') as file_out:
#     file_out.writelines(test)


# print(lines)
# print(len(lines))
# print(type(lines))




# filename = os.path.join(path,'week_09_files/weather_uk_100years.csv')
# with open(filename) as f:
#     content = f.read()
# print(content)
