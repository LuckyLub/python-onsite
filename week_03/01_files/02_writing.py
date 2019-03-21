'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

f1 = "Documents/The Marvellous Land of Oz.txt"
f2 = "Documents/zO fo dnaL suollevraM ehT .txt"

def rev(file1, file2):
    with open(file1, 'r') as file1:
        with open(file2, 'w') as file2:
            text_file1 = file1.read()
            new_file = text_file1[::-1]
            file2.write(new_file)

rev(f1, f2)