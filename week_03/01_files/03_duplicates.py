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


import hashlib
import os


#setting up the directory and subdirectories, and collecting all files.
directory = "ProjectDocuments/MP3"
dirs = [x[0] for x in os.walk(directory)]
files = [x[2] for x in os.walk(directory)]

#set up a dictionary which will help us return the duplicates.
files_by_path = {}

for i in range(files.__len__()):
    for j in range(files[i].__len__()):
        filepath = os.path.join(dirs[i], files[i][j])
        hash = hashlib.md5()

        #open the file in read modus and in binary. set a first chunk to be processed by the hash-function
        with open(filepath, "rb") as fin:
            chunck = fin.read(1024)

            # if i don't set a range, it keeps on running. I guess cause the files are too large?
            # chunks of the file are processed into a hash-function
            for r in range(100):
                hash.update(chunck)
                chunk = fin.read(1024)
            outcome_hash = hash.hexdigest()

            #now i add the hashvalues to a dictionary as a key, and set their path as value, so that we can see
            #which hashfunction is related to which paths.
            if outcome_hash in files_by_path.keys():
                files_by_path[outcome_hash].append(filepath)
            else:
                files_by_path[outcome_hash] = [filepath]

#now I check if there are multiple values to the same key. if that's the case, it are duplicates.
for v in files_by_path.values():
    if v.__len__() > 1:
        duplicates = "\n".join(str(x) for x in v)
        print(f"The following files are duplicates: {duplicates}")
