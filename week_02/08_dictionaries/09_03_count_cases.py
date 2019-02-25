'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''


def count_cases(text):
    lowercount = 0
    uppercount = 0
    punctcount = 0
    punctuations = [",", ".", "!", "?", ":", ";", "(", ")"]
    my_dict = {}

    for i in text:
        if i in punctuations:
            punctcount += 1
        elif i == i.lower():
            lowercount += 1
        elif i == i.upper():
            uppercount += 1

    my_dict["Upper case"] = uppercount
    my_dict["Lower case"] = lowercount
    my_dict["Punctuaction"] = punctcount
    return my_dict


text = input("Type a sentence, please:")
output = count_cases(text)
print(output)