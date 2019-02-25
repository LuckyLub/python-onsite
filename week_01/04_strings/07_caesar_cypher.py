



def rotate_word(word, key=1):
    new_word = str()
    for letter in word:
        new_word = new_word + chr(ord(letter) + key)
    return new_word

print(rotate_word("Sjaman", 8))

