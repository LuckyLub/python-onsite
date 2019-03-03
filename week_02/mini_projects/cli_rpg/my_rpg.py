import sys
import random
import time

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


intro_part1 = "----------------------------Welcome to Judith.----------------------------\n\n" \
              "The goal of this game is to rescue the princess Judith. This can only be \n" \
              "achieved when you've reached level 10 and conquered the villain of this\n" \
              "story:\n" \
              "                               Lazarus.\n\n" \


intro_part2 = "Let us begin the story." \
              "---------------------------------------------------------------------------" \

intro_part3 = "A long war was raging in the mainlands of Moracle. It lasted for almost 55\n" \
              "years and it didn't look like it was going to change any time soon.\n " \
              "King Josh had only reigned in times of war. He did not now any better. His \n" \
              "father died when he was only 14 years old, 30 years ago. Last of his\n" \
              "bloodline, he was strongly advised to mary as soon as he would turn 18. He\n " \
              "did. He married to Brigitte and together they got a girl, named Judith." \

intro_part4 = "While the war was raging on in the mainland, live on the coast was" \
              "relatively quiet.Focused on the war in the mainland"



for char in intro:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(5)

print()

