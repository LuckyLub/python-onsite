'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

flag = True
while flag:
    try:

        uin = int(input("Please, type in an integer."))

    except ValueError:

        print("That's no integer")

    else:
        print("Good job. That's an integer.")
        flag = False
