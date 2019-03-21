'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


def shortest_word(list_of_words):
    words_dict = {}
    shortest_words = []

    for word in list_of_words:
        words_dict[word] = word.__len__()

    shortest_size = min(words_dict.values())

    for k in words_dict.keys():
        if k.__len__() == shortest_size:
            shortest_words.append(k)

    return shortest_words

def longest_word(list_of_words):
    words_dict = {}
    longest_words = []

    for word in list_of_words:
        words_dict[word] = word.__len__()

    longest_size = max(words_dict.values())

    for k in words_dict.keys():
        if k.__len__() == longest_size:
            longest_words.append(k)

    return longest_words

with open("Documents/The Marvellous Land of Oz.txt") as file:
    text = file.read().split()

print(f"The shortest words fount are: {shortest_word(text)}")
print(f"The shortest words fount are: {longest_word(text)}")
print(f"Total number of words in the file are: {text.__len__()}")
