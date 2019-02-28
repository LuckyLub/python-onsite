'''
Write a function that takes in a list and finds the max, min, average and sum.

'''

def data_overview(list_):
    maximum = max(list_)
    minimum = min(list_)
    average = sum(list_)/len(list_)
    total_sum = sum(list_)
    print(f'The maximum value of your list is: {maximum}\n'
          f'The minimum value of your list is: {minimum}\n'
          f'The average value of your list is: {average}\n'
          f'The sum of your list is: {total_sum}')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data_overview(my_list)