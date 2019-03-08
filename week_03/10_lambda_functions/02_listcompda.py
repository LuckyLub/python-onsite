'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

print([x.startswith('D') for x in names])

mylambdaexp = lambda mylist: [name.startswith("D") for name in mylist]

print(mylambdaexp(names))