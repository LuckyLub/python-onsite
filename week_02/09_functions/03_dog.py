'''
Write a program with the following three functions:

    - bark - this function should not take in any arguments and should print the string "bark bark"
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

while True:
    bark()
    answer = input("The dog is telling you that he is hungry. Do you want to feed him? (yes/no)")
    if answer.lower() == "no":
        break
    else:
        food = input("What would you like to feed him?")
        amount = input(f'How many {food} do you want to give him?')
        eat(food, amount)
        print("That was some good stuff! He'll go for a nap now.")
        sleep()



