'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.

2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.
'''

class dog:

    def __init__(self, name, color, age, hungry=False, energy=100):
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = hungry
        self.energy = energy

    def sleep(self):
        self.is_hungry = True
        self.energy += 20

    def eat(self):
        self.is_hungry = False
        self.energy = 100

    def __str__(self):
        if self.is_hungry:
            hunger = ""
        else:
            hunger = "not "

        return (f"{self.name} is {self.color} and is {self.age} years old. The dog is {hunger}hungry and has "
              f"{self.energy} percent left of energy.")


rex = dog("Rex", "black", 10)
max = dog(name="Max", color="Brown", age=2, hungry=True, energy=20)

print(rex)
print(max)

for i in range(3):
    max.sleep()
    print(f"Energy: {max.energy}, Hungry: {max.is_hungry}")

max.eat()
print(f"Energy: {max.energy}, Hungry: {max.is_hungry}")