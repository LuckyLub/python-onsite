'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerator(itterable):
    i = 0
    list_ = []
    for item in itterable:
        index = i
        i += 1
        list_.append((index, item))
    return list_

my_list = [0,1,2,3,4,5,6,7,8,9]

print(my_enumerator(my_list))