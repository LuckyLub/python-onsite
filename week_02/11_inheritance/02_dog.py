'''

Building on the dog class from the previous example, create a subclass of the dog class
with at least one additional attribute. Also, override the sleep() and eat() methods to act
slightly different.

Create and object of this class and demonstrate it's functionality.

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

class handicapped_dog(dog):

    def __init__(self, name, color, age, handicap, hungry=False, energy=100):
        super().__init__(name, color, age, hungry, energy)
        self.handicap = handicap

    def sleep(self):
        self.is_hungry = True
        self.energy += 15

    def eat(self):
        self.is_hungry = False
        self.energy = 100

    def __str__(self):
        if self.is_hungry:
            hunger = ""
        else:
            hunger = "not "

        return (f"{self.name} is {self.color} and is {self.age} years old. The dog is {hunger}hungry and has "
              f"{self.energy} percent left of energy. It is a handicapped dog, its handicap is: {self.handicap}.")


Arnold = handicapped_dog("Arnold", "red", 7,"three legs")
Arnold.eat()
Arnold.eat()

print(Arnold)

