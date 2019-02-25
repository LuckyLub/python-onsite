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

    for i in my_dict:
        if my_dict[i] > 1:
            my_dict[i] = True
        else:
            my_dict[i] = False

    return my_dict

print(duplicate_checker(inputlist))