'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

import random

words=[]
words_document =open('/usr/share/dict/words')

for word in words_document:
    words.append(word.strip("\n"))

for i in range(10):
    print(f"#{words[random.randint(0,words.__len__()-1)]}")

