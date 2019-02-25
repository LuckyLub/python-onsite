'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''

def most_frequent(text):
    text_set = set(text)
    counter_list = []
    final_list = []

    for letter in text_set:
        counter_list.append([text.lower().count(letter), letter.lower()])
    counter_list.sort()

    for duo in counter_list:
        final_list.append(duo[1])

    return final_list


print(most_frequent("Here is some text I wrote today."))

