'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''


user_string = input("Write something!")
vowels = ["a", "e", "i", "o", "u"]


print(user_string.upper())
print(user_string.lower())

def vowel_lower_consonant_upper(sentence, letterlist):
    new_string = str()
    check = 0
    for letter1 in sentence:
        for letter2 in letterlist:
            if letter1.lower() == letter2.lower():
                new_string = new_string + letter1.lower()
                check = 1
        if check == 0:
            new_string = new_string + letter1.upper()
        else:
            check = 0
    return new_string


print(vowel_lower_consonant_upper(user_string, vowels))
