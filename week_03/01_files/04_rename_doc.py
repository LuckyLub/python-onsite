'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

def sed(pattern, replacement, file1, file2):
    with open(file1, 'r') as file1:
        with open(file2, 'w') as file2:
            text_file1 = file1.read()
            new_text = text_file1.replace(pattern, replacement)
            file2.write(new_text)

f1 = "ProjectDocuments/The Marvellous Land of Oz.txt"
f2 = "ProjectDocuments/CoppiedAdjustOzToMordor.txt"
p = "Oz"
r = "Mordor"

sed(p,r,f1,f2)