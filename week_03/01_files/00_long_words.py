'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

with open("ProjectDocuments/The Marvellous Land of Oz.txt") as file:
    text = file.read().split()

word_count ={}

for word in text:
    if word.__len__() > 20:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)