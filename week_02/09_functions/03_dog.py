'''
Write a program with the following three functions:

    - bark - this method should not take in any arguments and should print the string "bark bark"
    - eat - takes in parameters food_item and amount and prints out "The dog ate <amount> of <food_item>
    - sleep - calls the python sleep method to sleep the program for 5 seconds.



'''


def bark():
    print("bark bark")


def eat(food_item, amount):
    print(f"The dog ate {amount} of {food_item}.")


def sleep():
    from time import sleep
    sleep(5)

