'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


# import hashlib
import os

# def duplicate_checker(dir, fileformat):
#     list_dir = os.walk(dir)
#     files = [x[2] for x in os.walk(dir)][x[2] for x in os.walk(dir)]
#     for file in files[0]:
#         with open(file, 'r') as openfile:
#             file_content = openfile.read()
#             m = hashlib.sha3_224()
#             m.update(file_content)
#             m.digest()
#             print(m)




directory = "ProjectDocuments/MP3"
a = [x[0] for x in os.walk(directory)]
b = [x[1] for x in os.walk(directory)]
c = [x[2] for x in os.walk(directory)]
files = []

for i in range(c.__len__()):
    for j in range(c[i].__len__()):
        # print("i",i, "j", j)
        # print("a",a[i])
        # print("c",c[i][j])
        files.append(str(a[i]+"/"+c[i][j]))


print("a", a)
print("b", b)
print("c", c)
print(files)
print(c.__len__())
print(c[0].__len__())

a=1

# duplicate_checker(directory,10)