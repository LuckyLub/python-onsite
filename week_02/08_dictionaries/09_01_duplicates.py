'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''

inputlist = ["a", "b", "c", "c"]


def duplicate_checker(user_list):
    my_dict = {}
    for i in user_list:
        my_dict[i] = 0

    for i in user_list:
        my_dict[i] += 1
        if my_dict[i] > 1:
            return True

    return False



print(duplicate_checker(inputlist))