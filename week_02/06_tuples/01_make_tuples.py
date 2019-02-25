'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''


def my_sorter(numbers_list):
    numbers_list.sort()
    if numbers_list.__len__() % 2 != 0:
        numbers_list.append(0)
    my_range = numbers_list.__len__()
    new_list = []
    for i in range(0,my_range, 2):
        a = (numbers_list[i],numbers_list[i+1])
        new_list.append(a)
    return new_list

numbers = [10, 1, 35 ,89, 33]

print(my_sorter(numbers))