'''
Write a script that finds the first vowel in a a user inputted string.

'''

user_input = input("Feed me some text. I'm going to return the first vowel.")
vowels = ["a", "e", "i", "o", "u"]

def first_vowel_checker(sentence, letterlist):
    for letter1 in sentence:
        for letter2 in letterlist:
            if letter1.lower() == letter2.lower():
                return f"The first vowel found is '{letter1}' at index {sentence.find(letter1)}."

print(first_vowel_checker(user_input,vowels))

