'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def kwargs_demonstrating(**kwargs):
    for k, v in kwargs.items():
        print(f"This keyword {k}, has this value {v}")


kwargs_demonstrating(name="Robert", age=28)