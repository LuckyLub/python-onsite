'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''


def guess_the_number():
    import random

    computer_number = random.randint(0, 100)
    turn = 1
    guesses = []
    persons_guess = int(input("The computer came up with a number between 1 and 100. Which one do you guess?"))
    while True:
        guesses.append(persons_guess)
        if computer_number > persons_guess:
            print("It's bigger than that!")
        elif computer_number < persons_guess:
            print("It's smaller than that!")
        else:
            print(f"Yes you won! You have guessed the number in {turn} turns.")
            return turn
        turn += 1
        persons_guess = int(input(f"Have another guess! Your guesses so far were: {', '.join(str(x) for x in guesses)}."))



a = guess_the_number()

