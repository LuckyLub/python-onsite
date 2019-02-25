'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]

list_[2] = list_[2][0] + list_[2][1]
list_[3] = list_[3][0] + list_[3][1]

print(list_)