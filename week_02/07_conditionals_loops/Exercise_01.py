'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''

user_number = int(input("Give me a number between 1 and 1.000.000!"))

while user_number < 0 or user_number > 1000000:
    user_number = int(input("That's an invalid number. Give me a number between 1 and 1.000.000!"))

if user_number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")
