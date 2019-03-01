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

print("aaaaaaaa")

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
results_list = [[],[],]


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
        results_list[strategy-1].append([turn, new_guess])

print(results_list)



count_list_strategy_1 = {}
count_list_strategy_2 = {}

outcome_list1 = []
outcome_list2 = []
outcome_list3 = []

for item in results_list[0]:
    outcome_list1.append(item[0])

for item in results_list[1]:
    outcome_list2.append(item[0])


#
# for item in results_list[0]:
#     if item[1] in count_list_strategy_1.keys():
#         count_list_strategy_1[item[1]] += 1
#     else:
#         count_list_strategy_1[item[1]] = 1
#
#
#     elif item[0] == 2:
#         if item[1] in count_list_strategy_2.keys():
#             count_list_strategy_2[item[1]] += 1
#         else:
#             count_list_strategy_2[item[1]] = 1


# print(outcome_list1)
# print(outcome_list2)




# Overlay 2 histograms to compare them
def overlaid_histogram(data1, data2, n_bins = 0, data1_name="", data1_color="#539caf", data2_name="", data2_color="#7663b0",x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 10
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins


    if n_bins == 0:
    	bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    else:
    	bins = n_bins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins = 20, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(data2, bins = 7, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')

overlaid_histogram(outcome_list1,outcome_list2, 10, data1_name="results strategy 1", data2_name="results strategy 2")

print("123")