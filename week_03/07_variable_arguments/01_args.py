'''
Write a script with a function that demonstrates the use of *args.

'''

def demonstrating_args(*args):

    for arg in args:
        print(f"This is something that you inputted: {arg}")

demonstrating_args(1,2,3,4,5,6)