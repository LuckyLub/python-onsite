import random

class Hero:

    def __init__(self, name="Caldor", race="Elf", gender="male", skill_set="archer", country="Elvengard"):
        self.name = name
        self.race = race
        self.gender = gender.lower()
        self.country = country
        self.skill_set = skill_set
        self.live = 100
        self.power = 10
        self.level = 1
        self.progress = 0

    def __str__(self):
        if self.gender == "male":
            person = "he"
        else:
            person = "she"

        return f"This is {self.name} the {self.race} from {self.country}.\n" \
            f"{person.capitalize()} is a level {self.level} type {self.skill_set}.\n" \
            f"{person.capitalize()} has {self.live} live left." \
            f"{person.capitalize()} needs {100 - self.progress} to reach the next level."

    def run_away(self):
        print(f"{self.name} is trying to run away.")
        outcome_hero = random.randint(1,6)
        if outcome_hero >= 3:
            self.progress -= 2
            if self.progress < 0:
                self.progress = 0
            return "won"
        else:
            return "lost"

    def attack(self):
        outcome_hero = random.randint(1,6)
        outcome_opponent = random.randint(1,6)
        if outcome_hero > outcome_opponent:
            return "won"
        else:
            return "lost"



class Opponent:

    def __init__(self):
        self.live = 100
        self.power = 10

