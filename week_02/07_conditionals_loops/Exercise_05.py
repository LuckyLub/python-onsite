'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''



def bound_sum(lower, upper):
    total = 0
    for i in range (lower, upper+1, 1):
        total += i
    average = total/(upper-lower+1)

    return total, average

print(bound_sum(int(input("Give a lower bound.")),int(input("Give a upper bound."))))
