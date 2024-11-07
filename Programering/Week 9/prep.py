# import os
# cwd = os.getcwd()
# print(cwd)

# import os
# for fi in os.listdir():
#     print(fi)

import os
for fi in os.listdir():
    if os.path.isdir(fi):
        print(fi, 'is a directory')
    elif os.path.isfile(fi):
        print(fi, 'is a file')
    else:
        print(fi, 'is not a directory or a file')