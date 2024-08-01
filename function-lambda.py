#  DESCRIPTION Learn Python lambda functions through pop culture examples, from simple to advanced levels.

# MARKDOWN CELL
# Python Lambda Functions: From Simple to Advanced

# Let's explore Python lambda functions through fun examples inspired by pop culture, music, movies, and more!

# MARKDOWN CELL
## Very Simple Examples

# MARKDOWN CELL
### 1. The Beatles Song Reverser

# CODE CELL
# Simple lambda to reverse a Beatles song title
reverse_song = lambda song: song[::-1]

print(reverse_song("Hey Jude"))
print(reverse_song("Yellow Submarine"))

# This lambda function takes a song title and reverses it.
# It uses string slicing with a step of -1 to reverse the string.

# MARKDOWN CELL
### 2. Pac-Man Power Pellet Multiplier

# CODE CELL
# Multiply Pac-Man's score when he eats a power pellet
power_pellet_bonus = lambda score: score * 2

print(power_pellet_bonus(100))
print(power_pellet_bonus(50))

# This lambda function doubles Pac-Man's score when he eats a power pellet.
# It takes the current score and multiplies it by 2.

# MARKDOWN CELL
### 3. Star Wars Lightsaber Color Checker

# CODE CELL
# Check if a lightsaber color is associated with the Jedi
is_jedi_color = lambda color: color.lower() in ['blue', 'green', 'purple']

print(is_jedi_color("Blue"))
print(is_jedi_color("Red"))

# This lambda function checks if a given lightsaber color is typically associated with the Jedi.
# It converts the input to lowercase and checks if it's in the list of Jedi colors.

# MARKDOWN CELL
## Simple Examples

# MARKDOWN CELL
### 1. Back to the Future Time Difference Calculator

# CODE CELL
# Calculate the time difference in Back to the Future
time_difference = lambda present, past: abs(present - past)

print(time_difference(1985, 1955))
print(time_difference(2015, 1985))

# This lambda calculates the absolute time difference between two years.
# It uses the abs() function to ensure the result is always positive.

# MARKDOWN CELL
### 2. Teenage Mutant Ninja Turtles Pizza Topping Counter

# CODE CELL
# Count the number of toppings on a TMNT pizza
topping_counter = lambda *toppings: len(toppings)

print(topping_counter("pepperoni", "mushroom", "olive"))
print(topping_counter("cheese", "anchovies"))

# This lambda uses *args to accept any number of toppings and count them.
# It simply returns the length of the tuple of toppings.

# MARKDOWN CELL
### 3. Ghostbusters Proton Pack Charge Level

# CODE CELL
# Calculate the charge level of a Ghostbusters proton pack
charge_level = lambda time, rate: min(100, time * rate)

print(charge_level(5, 15))
print(charge_level(10, 12))

# This lambda calculates the charge level based on time and rate, capped at 100%.
# It uses the min() function to ensure the charge never exceeds 100%.

# MARKDOWN CELL
## Intermediate Examples

# MARKDOWN CELL
### 1. Matrix Pill Effectivity Calculator

# CODE CELL
# Calculate the effectivity of red and blue pills from The Matrix
pill_effect = lambda red, blue: (lambda x: x * 2 if red else x / 2 if blue else x)

neo_power = pill_effect(True, False)
print(neo_power(50))

morpheus_power = pill_effect(False, True)
print(morpheus_power(50))

# This lambda creates another lambda function based on pill colors.
# It doubles the value for red, halves for blue, and leaves unchanged otherwise.

# MARKDOWN CELL
### 2. Jurassic Park DNA Sequence Matcher

# CODE CELL
# Check if a DNA sequence matches a dinosaur species
dna_matcher = lambda sequence: {
    "TGCA": "T-Rex",
    "CAGT": "Velociraptor",
    "ATGC": "Brachiosaurus"
}.get(sequence, "Unknown")

print(dna_matcher("TGCA"))
print(dna_matcher("ATGC"))
print(dna_matcher("GGTT"))

# This lambda uses a dictionary to match DNA sequences to dinosaur species.
# The .get() method returns "Unknown" if the sequence isn't found.

# MARKDOWN CELL
### 3. Star Trek Universal Translator

# CODE CELL
# Translate English to Star Trek alien languages
universal_translator = lambda text, language: {
    "Klingon": f"tlhIngan Hol: {text}",
    "Vulcan": f"Vulcan: {text.lower()}",
    "Ferengi": f"Ferengi: {text.upper()}"
}.get(language, f"Unknown language: {text}")

print(universal_translator("Hello", "Klingon"))
print(universal_translator("Live long and prosper", "Vulcan"))
print(universal_translator("Show me the money", "Ferengi"))

# This lambda simulates a universal translator using a dictionary.
# It applies different text transformations based on the alien language.

# MARKDOWN CELL
## Advanced Examples

# MARKDOWN CELL
### 1. Inception Dream Level Calculator

# CODE CELL
import time

# Calculate dream time dilation in Inception
dream_time = lambda levels: (lambda real_time: 
                             real_time * 60**levels)

level1 = dream_time(1)
level2 = dream_time(2)
level3 = dream_time(3)

real_time = 5  # 5 minutes in real time
print(f"5 minutes in reality is:")
print(f"Level 1 dream: {level1(real_time)} minutes")
print(f"Level 2 dream: {level2(real_time)} minutes")
print(f"Level 3 dream: {level3(real_time)} minutes")

# This lambda creates another lambda that calculates dream time based on levels.
# It uses exponential time dilation as seen in the movie Inception.

# MARKDOWN CELL
### 2. Marvel Cinematic Universe Timeline Sorter

# CODE CELL
# Sort Marvel movies by in-universe chronological order
mcu_sorter = lambda movies: sorted(movies, key=lambda movie: movie[1])

mcu_movies = [
    ("Iron Man", 2010),
    ("Captain America: The First Avenger", 1942),
    ("Captain Marvel", 1995),
    ("Black Widow", 2020),
    ("Avengers: Endgame", 2023)
]

sorted_movies = mcu_sorter(mcu_movies)
for movie, year in sorted_movies:
    print(f"{movie}: {year}")

# This lambda uses the sorted() function with a key function to sort movies.
# The key function is another lambda that extracts the year from each movie tuple.

# MARKDOWN CELL
### 3. Hogwarts House Points Calculator

# CODE CELL
# Calculate and update Hogwarts house points
house_points = {"Gryffindor": 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin": 0}

update_points = lambda house, points: house_points.update({house: house_points.get(house, 0) + points}) or house_points

print(update_points("Gryffindor", 50))
print(update_points("Slytherin", 20))
print(update_points("Gryffindor", -10))
print(update_points("Ravenclaw", 30))

# This lambda updates the house points and returns the updated dictionary.
# It uses the or operator to return the dictionary after the update.

# MARKDOWN CELL
## Very Advanced Examples

# MARKDOWN CELL
### 1. Rick and Morty Multiverse Channel Surfer

# CODE CELL
import random

# Simulate interdimensional cable surfing from Rick and Morty
def generate_show():
    adjectives = ["Interdimensional", "Quantum", "Galactic", "Cyborg", "Alien"]
    nouns = ["Adventures", "Cooking", "Wrestling", "Dating", "Court"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

channel_surfer = lambda n: (lambda: [generate_show() for _ in range(n)])

surf_3_channels = channel_surfer(3)
surf_5_channels = channel_surfer(5)

print("Surfing 3 channels:", surf_3_channels())
print("Surfing 5 channels:", surf_5_channels())

# This advanced lambda creates another lambda that generates random TV shows.
# It simulates the interdimensional cable from Rick and Morty.

# MARKDOWN CELL
### 2. Thanos Snap Universe Balancer

# CODE CELL
import random

# Simulate Thanos' snap from Avengers: Infinity War
universe = ["Iron Man", "Captain America", "Thor", "Black Widow", "Hulk", "Hawkeye", 
            "Spider-Man", "Black Panther", "Doctor Strange", "Scarlet Witch"]

thanos_snap = (lambda population: 
               lambda: list(filter(lambda _: random.random() > 0.5, population)))

balanced_universe = thanos_snap(universe)

print("Before the snap:", universe)
print("After the snap:", balanced_universe())

# This lambda creates another lambda that simulates Thanos' snap.
# It uses filter with a random condition to eliminate half the population.

# MARKDOWN CELL
### 3. Doctor Who TARDIS Time-Space Coordinate Calculator

# CODE CELL
from functools import reduce

# Calculate TARDIS coordinates across time and space
tardis_coordinates = lambda *trips: reduce(lambda acc, trip: 
                                           (acc[0] + trip[0], acc[1] + trip[1], 
                                            acc[2] + trip[2], acc[3] + trip[3]), 
                                           trips, (0, 0, 0, 0))

# Each trip is (time_shift, x, y, z)
gallifrey_trip = (10000, 5000, -3000, 8000)
earth_2023_trip = (-9977, -4995, 3005, -7995)
moon_landing_trip = (-54, -2, 1, -3)

final_coordinates = tardis_coordinates(gallifrey_trip, earth_2023_trip, moon_landing_trip)
print(f"Final TARDIS coordinates (time, x, y, z): {final_coordinates}")

# This complex lambda uses reduce with another lambda to calculate cumulative coordinates.
# It simulates the TARDIS traveling through time and space in Doctor Who.

# MARKDOWN CELL
# Congratulations! You've mastered Python lambda functions across various complexity levels.
# Keep exploring and may the force of functional programming be with you!