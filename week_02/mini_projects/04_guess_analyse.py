'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random
import numpy as np
import matplotlib.pyplot as plt

plt.interactive(True)


def get_number(minimum, maximum):

    return random.randint(minimum, maximum)


def check_number(computer_number, persons_guess):

    if computer_number > persons_guess:
        return "higher"

    elif computer_number < persons_guess:
        return "lower"

    else:
        return "won"


def guess_determination(hint, strategy, minimum_range, maximum_range, turn=0, previous_guesses =[]):

    if strategy == 1:
        if turn == 0:
            new_guess = 1

        else:
            new_guess = minimum_range + 1

        return new_guess

    if strategy == 2:
        new_guess = round(minimum_range + ((maximum_range-minimum_range)/2))
        return new_guess



strategy_list = [1,2]
attempts = 10000
results_list = [[],[]]
min_range_computer = 1
max_range_computer = 200
turn = 0


for strategy in strategy_list:
    for attempt in range(attempts):
        computer_number = get_number(min_range_computer, max_range_computer)
        new_guess = guess_determination(None, strategy, min_range_computer, max_range_computer)
        turn = 1
        result = check_number(computer_number, new_guess)

        if result == "lower":
            max_guess = new_guess
            min_guess = min_range_computer - 1
        else:
            min_guess = new_guess
            max_guess = max_range_computer


        while result != "won":
            new_guess = guess_determination(result, strategy, min_guess, max_guess, turn)
            turn += 1
            result = check_number(computer_number, new_guess)

            if result == "lower":
                max_guess = new_guess

            else:
                min_guess = new_guess

        results_list[strategy-1].append([turn, new_guess])


outcome_list1 = []
outcome_list2 = []

average_turns1 = 0
average_turns2 = 0

for item in results_list[0]:
    outcome_list1.append(item[0])
    average_turns1 += item[0]
average_turns1 = average_turns1/results_list[0].__len__()

for item in results_list[1]:
    outcome_list2.append(item[0])
    average_turns2 += item[0]
average_turns2 = average_turns2/results_list[0].__len__()

print(f"Average turns Strategy 1: {average_turns1}")
print(f"Average turns Strategy 2: {average_turns2}")


# Overlay 2 histograms to compare them
def overlaid_histogram(data1, data2, data1_name="", data1_color="#539caf", data2_name="", data2_color="#7663b0",x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 10
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins = 10, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(data2, bins = 9, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')

overlaid_histogram(outcome_list1,outcome_list2, 10, data1_name="results strategy 1", data2_name="results strategy 2")

print("123")