'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''


def bound_sqr(lower, upper):
    output =[]
    for i in range(lower, upper+1, 1):
        output.append(i**2)
    return output


print(bound_sqr(int(input("Give a lower bound.")),int(input("Give a upper bound."))))