def rotate_word(word, key=1):
    new_word = str()
    for letter in word.lower():

        letter_index = ord(letter)-ord("a")

        if key < 0:
            key = 26 - ((-key) % 26)

        new_word = new_word + chr(ord("a") + ((letter_index + key) % 26))

    return new_word

print(rotate_word("Melon", 16))
