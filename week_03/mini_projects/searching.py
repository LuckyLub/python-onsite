'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''

import os

start_folder = "/home/robert-jan"

my_dictionary = {}
dirs = [file[0] for file in os.walk(start_folder)]
files = [file[2] for file in os.walk(start_folder)]

for index, dir in enumerate(dirs):
    for file in files[index]:
        if file[-3:] == "jpg":
            if dir not in my_dictionary.keys():
                my_dictionary[dir]= []
            my_dictionary[dir].append(file)

print(my_dictionary)

