'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random

def get_number():
    return random.randint(1,100)

def check_number(computer_number, persons_guess):
    while True:
        if computer_number > persons_guess:
            return "higher"
        elif computer_number < persons_guess:
            return "lower"
        else:
            return "won"

def guess_determination(hint, strategy, turn=0, previous_guesses =[]):

    if strategy == 1:
        if turn == 0:
            new_guess = 1
        else:
            new_guess = previous_guesses[previous_guesses.__len__()-1] + 1

        return new_guess

    if strategy == 2:
        correction_list = [25, 13, 6, 3,1,1,1]

        if turn == 0:
            new_guess = 50
            return new_guess
        elif hint == "lower":
            new_guess = previous_guesses[previous_guesses.__len__()-1] - correction_list[turn-1]
        else:
            new_guess = previous_guesses[previous_guesses.__len__()-1] + correction_list[turn-1]
        return new_guess

strategy_list = [1,2]
attempts = 1000
results_list = []


for strategy in strategy_list:
    for attempt in range(attempts):
        guesses = []
        computer_number = get_number()
        new_guess = guess_determination(None, strategy)
        guesses.append(new_guess)
        result = check_number(computer_number,new_guess)
        turn = 1
        while result != "won":
            new_guess = guess_determination(result, strategy,turn,guesses)
            guesses.append(new_guess)
            result = check_number(computer_number, new_guess)
            turn += 1
            # print("computer", computer_number)
            # print("guess", new_guess)
            # print(strategy, turn, result)
        results_list.append((strategy, turn, new_guess))

print(results_list)

import matplotlib
