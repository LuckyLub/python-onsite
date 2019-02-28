
'''
Flush out the classes below with the following:

    - Add inheritance so that Class1 is inherited by Class2 and Class2 is inherited by Class3.
    - Follow the directions in each class to complete the functionality.



'''

class Class1:


    # define an __init__() method that sets an attribute x
    def __init__(self):
        self.x = 10


class Class2(Class1):

    # define an __init__() method that sets an attribute y and calls the __init__() method of its parent
    def __init__(self):
        super().__init__()
        self.y = 100

class Class3(Class2):

    # define an __init__() method that sets an attribute z and calls the __init__() method of its parent
    def __init__(self):
        super().__init__()
        self.z = 1000


# create an object of each class and print each of its attributes

a = Class1()
print(a.x)

b = Class2()
print(b.x, b.y)

c = Class3()
print(c.x, c.y, c.z)
