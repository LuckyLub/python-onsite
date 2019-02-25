'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

equals = []
differents = []

for one in list_one:
    check = 0
    for two in list_two:
        if one == two:
            equals.append(one)
            check = 1
    if check == 0:
        differents.append(one)

for two in list_two:
    check = 0
    for equal in equals:
        if two == equal:
            check = 1
    if check == 0:
        differents.append(two)

print(equals)
print(differents)

