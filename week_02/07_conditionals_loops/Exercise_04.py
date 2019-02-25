'''
Print out every prime number between 1 and 100.

'''

for i in range(1, 100):

    x = 0
    for j in range(1, i):
        if not(j == 1):
            if i % j == 0:
                x += 1

    if x < 1:
        print(i)
