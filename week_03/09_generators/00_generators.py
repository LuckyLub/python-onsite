'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

my_gen = (i**2 for i in range(4))

my_results = (i**2 for i in my_gen)

print(my_gen)
# print([i for i in my_gen])
# print([i for i in my_gen])
print([i for i in my_results])