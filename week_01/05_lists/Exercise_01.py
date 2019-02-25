'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

amount_of_numbers = 10
numbers_list=[]
total = float()

for i in range (amount_of_numbers):
    total += float(input(f"Feed me a number (can be float). {i+1}/{amount_of_numbers}"))

print(f'Total sum equals: {total}')
print(f'Average of all numbers equals: {total/amount_of_numbers}')
