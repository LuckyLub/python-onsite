'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

flag = True
while flag:

    try:
        num1 = float(input("Give me your first number."))
        num2 = float(input("Give me your second number."))

    except ValueError:
        print("That is an incorrect input, please make sure your input are numbers.")

    else:
        try:
            print(num1/num2)

        except ZeroDivisionError:
            print("You can't devide by zero.")

        else:
            flag = False



