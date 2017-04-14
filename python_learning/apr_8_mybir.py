# import os
# def tellos() :
#     print(os.name)
#     #os.uname()
#     #os.unname()doesn't exist on Windows
# tellos()
# print(os.environ.get('PATH'))
# #os.mkdir(r'./create_directory')
# #os.mkdir(r'./aa')
# dirlist=[ x for x in os.listdir(r'.') if os.path.isdir(x)]
# filewithpy=[x for x in os.listdir(r'.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(dirlist)
# print(filewithpy)

import os

file_path_list = []
def find_all_files(path) :
    for x in os.listdir(path) :
        if os.path.isfile(os.path.join(path,x)) :
            file_path_list.append(x)
        elif os.path.isdir(x) :
            find_all_files(x)
    return file_path_list
# find_all_files(r'.')
# print(file_path_list)
print(find_all_files('.'))