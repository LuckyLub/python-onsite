'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''

verses = "\nOld Old MacDonald had a farm" \
         "\nE-I-E-I-O"
animal_list = []

print("You are going to make your own Old MacDonald song. Whenever you want to quit, type 'quit'.\n")


print(verses)
animal = input("What kind of animal did he have?")

status ="go"
while status == "go":
    if animal.lower() == 'quit':
        print("Thanks for singing along!")
        exit()
    sound = input("What kind of sound does it make?")
    if sound.lower() == 'quit':
        print("Thanks for singing along!")
        exit()
    animal_list.append((animal, sound))

    for animal in animal_list:
        print(verses)
        print(f"\nAnd on this farm he had a {animal[0]}"
              f"\nE-I-E-I-O"
              f"\nWith a {animal[1]} {animal[1]} here"
              f"\nAnd a {animal[1]} {animal[1]} there"
              f"\nHere a {animal[1]}, there a {animal[1]}"
              f"\nEverywhere a {animal[1]} {animal[1]}")
        print(verses)





