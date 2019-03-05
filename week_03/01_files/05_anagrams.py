'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

import anagram_creator

def store_anagrams(anagram_dict, shelf):
    shelf.append(anagram_dict)

def read_anagrams(word, anagram_dict):
    for v in anagram_dict.values():
        for item in v:
            if item == word:
                return v


shelf1 = []
anagram_map = anagram_creator.all_anagrams('words.txt')
anagram_creator.print_anagram_sets_in_order(anagram_map)
store_anagrams(anagram_map, shelf1)
print(read_anagrams("aah",anagram_map))

# eight_letters = anagram_creator.filter_length(anagram_map, 8)
# anagram_creator.print_anagram_sets_in_order(eight_letters)