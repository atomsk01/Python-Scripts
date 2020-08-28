#!/usr/bin/python3

#create a mad libs story teller!
#use the magic 8 ball script for reference
#use the prewritten story 
#create tuples() for season, superhero, animal, people, verb, and places.

#dont forget to import random!
import random

season = ("spring", "summer", "winter", "fall")
superHero = ("He-Man", "Powdered Toast Man", "Captain Planet", "Darkwing Duck")
animal = ("cat", "dog", "goat", "fox")
people = ("Jessie", "James", "Franklin", "Bejamin")
verb = ("fly", "eat", "dance", "skip")
place = ("Bakersfield", "my neighbor's backyard", "over there", "the sewers")
#implement the random function
value = random.randint(0, 3)

#heres the story
#use {tuple[value]} to import from the tuples above
#use f to treat the {} as python code
print(f"Every {season[value]}, {superHero[value]} is joined by the {animal[value]}, who's secret identity is {people[value]}.")
print(f"They attempt to {verb[value]}, which rarely succeds.")
print(f"So instead, they chase down a villain in {place[value]}.")

