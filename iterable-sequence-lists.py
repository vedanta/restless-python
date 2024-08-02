#  DESCRIPTION Explore Python lists through pop culture examples, from simple operations to advanced techniques.

# MARKDOWN CELL
# Python Lists: From Simple to Advanced

# Let's dive into Python lists with fun examples inspired by pop culture, music, movies, and more!

# MARKDOWN CELL
## Very Simple Examples

# MARKDOWN CELL
### 1. Creating a List of Avengers

# CODE CELL
# Create a list of Avengers
avengers = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye"]

print("Original Avengers team:", avengers)
print("Number of Avengers:", len(avengers))

# This example shows how to create a list and use the len() function to get its length.

# MARKDOWN CELL
### 2. Accessing Hogwarts Houses

# CODE CELL
# Access elements in a list of Hogwarts houses
hogwarts_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

print("First house:", hogwarts_houses[0])
print("Last house:", hogwarts_houses[-1])

# This demonstrates how to access list elements using positive and negative indices.

# MARKDOWN CELL
### 3. Adding Pokémon to a List

# CODE CELL
# Add Pokémon to a list
pokemon = ["Pikachu", "Charizard", "Bulbasaur"]
print("Initial Pokémon:", pokemon)

pokemon.append("Squirtle")
print("After appending Squirtle:", pokemon)

pokemon.insert(1, "Gengar")
print("After inserting Gengar at index 1:", pokemon)

# This example shows how to add elements to a list using append() and insert() methods.

# MARKDOWN CELL
## Simple Examples

# MARKDOWN CELL
### 1. Removing Star Wars Planets

# CODE CELL
# Remove planets from a list of Star Wars locations
planets = ["Tatooine", "Hoth", "Dagobah", "Endor", "Naboo", "Coruscant", "Kamino"]
print("Original planets:", planets)

# Remove the last planet
removed_planet = planets.pop()
print("Removed planet:", removed_planet)
print("Planets after pop():", planets)

# Remove a specific planet
planets.remove("Hoth")
print("Planets after removing Hoth:", planets)

# Remove a planet by index
del planets[1]
print("Planets after deleting index 1:", planets)

# This example demonstrates different ways to remove elements from a list.

# MARKDOWN CELL
### 2. Slicing Jurassic Park Dinosaurs

# CODE CELL
# Slice a list of Jurassic Park dinosaurs
dinosaurs = ["Tyrannosaurus", "Velociraptor", "Brachiosaurus", "Triceratops", "Dilophosaurus", "Pteranodon"]

print("All dinosaurs:", dinosaurs)
print("First three dinosaurs:", dinosaurs[:3])
print("Last two dinosaurs:", dinosaurs[-2:])
print("Every other dinosaur:", dinosaurs[::2])

# This shows how to use list slicing to extract portions of a list.

# MARKDOWN CELL
### 3. Modifying Marvel Superhero Teams

# CODE CELL
# Modify lists of Marvel superhero teams
avengers = ["Iron Man", "Thor", "Hulk"]
guardians = ["Star-Lord", "Gamora", "Drax", "Rocket", "Groot"]

# Combine teams
all_heroes = avengers + guardians
print("Combined team:", all_heroes)

# Create copies
avengers_copy = avengers.copy()
guardians_copy = guardians[:]

# Modify copies
avengers_copy.extend(["Black Widow", "Hawkeye"])
guardians_copy[0] = "Peter Quill"

print("Modified Avengers copy:", avengers_copy)
print("Modified Guardians copy:", guardians_copy)
print("Original Avengers (unchanged):", avengers)
print("Original Guardians (unchanged):", guardians)

# This example shows list concatenation, copying, and modification.

# MARKDOWN CELL
## Intermediate Examples

# MARKDOWN CELL
### 1. Sorting and Reversing Lord of the Rings Characters

# CODE CELL
# Sort and reverse a list of Lord of the Rings characters
characters = ["Frodo", "Samwise", "Aragorn", "Legolas", "Gimli", "Gandalf", "Boromir"]

# Sort the list
sorted_characters = sorted(characters)
print("Sorted characters:", sorted_characters)

# Reverse the list
characters.reverse()
print("Reversed original list:", characters)

# Sort in reverse order
reverse_sorted = sorted(characters, reverse=True)
print("Reverse sorted:", reverse_sorted)

# This example demonstrates sorting and reversing lists.

# MARKDOWN CELL
### 2. List Comprehension with Pokémon Types

# CODE CELL
# Use list comprehension with Pokémon types
pokemon_types = [
    ("Pikachu", "Electric"),
    ("Charizard", "Fire/Flying"),
    ("Bulbasaur", "Grass/Poison"),
    ("Squirtle", "Water"),
    ("Gengar", "Ghost/Poison")
]

# Get all Pokémon names
pokemon_names = [pokemon[0] for pokemon in pokemon_types]
print("Pokémon names:", pokemon_names)

# Get Pokémon with multiple types
multi_type_pokemon = [name for name, type in pokemon_types if "/" in type]
print("Multi-type Pokémon:", multi_type_pokemon)

# This shows how to use list comprehensions for filtering and transforming data.

# MARKDOWN CELL
### 3. Nested Lists with Hogwarts Students

# CODE CELL
# Work with nested lists of Hogwarts students
hogwarts_students = [
    ["Harry Potter", "Hermione Granger", "Ron Weasley"],
    ["Draco Malfoy", "Vincent Crabbe", "Gregory Goyle"],
    ["Luna Lovegood", "Cho Chang", "Cedric Diggory"]
]

# Access nested elements
print("First Gryffindor student:", hogwarts_students[0][0])
print("Last Ravenclaw/Hufflepuff student:", hogwarts_students[2][-1])

# Flatten the nested list
all_students = [student for house in hogwarts_students for student in house]
print("All students:", all_students)

# This demonstrates working with nested lists and flattening them.

# MARKDOWN CELL
## Advanced Examples

# MARKDOWN CELL
### 1. Custom Sorting with Star Wars Bounty Hunters

# CODE CELL
from operator import itemgetter

# Custom sorting of Star Wars bounty hunters
bounty_hunters = [
    ("Boba Fett", 150000, 5),
    ("Bossk", 120000, 3),
    ("Dengar", 100000, 2),
    ("IG-88", 140000, 4),
    ("Zuckuss", 90000, 2)
]

# Sort by bounty (descending), then by reputation
sorted_hunters = sorted(bounty_hunters, key=itemgetter(1, 2), reverse=True)

print("Sorted Bounty Hunters:")
for hunter in sorted_hunters:
    print(f"{hunter[0]}: {hunter[1]} credits, {hunter[2]} star reputation")

# This shows advanced sorting using the itemgetter function.

# MARKDOWN CELL
### 2. List as a Stack and Queue (Time Travel Device)

# CODE CELL
from collections import deque

# Implement a time travel device using a list as a stack and a deque as a queue
class TimeMachine:
    def __init__(self):
        self.past_events = []  # Stack for past events
        self.future_events = deque()  # Queue for future events

    def travel_to_past(self, event):
        self.past_events.append(event)
        print(f"Traveled to: {event}")

    def return_to_present(self):
        if self.past_events:
            event = self.past_events.pop()
            print(f"Returned from: {event}")
        else:
            print("Already in the present!")

    def schedule_future(self, event):
        self.future_events.append(event)
        print(f"Scheduled future event: {event}")

    def travel_to_future(self):
        if self.future_events:
            event = self.future_events.popleft()
            print(f"Traveled to future event: {event}")
        else:
            print("No future events scheduled!")

# Use the TimeMachine
doctor_who = TimeMachine()

doctor_who.travel_to_past("Ancient Rome")
doctor_who.travel_to_past("Jurassic Period")
doctor_who.return_to_present()
doctor_who.schedule_future("Mars Colony")
doctor_who.schedule_future("Galactic Federation")
doctor_who.travel_to_future()

# This advanced example uses a list as a stack and a deque as a queue to simulate a time machine.

# MARKDOWN CELL
### 3. List Filtering and Mapping with Superhero Teams

# CODE CELL
# Filter and map operations on superhero teams
heroes = [
    {"name": "Iron Man", "team": "Avengers", "power": 85},
    {"name": "Black Widow", "team": "Avengers", "power": 75},
    {"name": "Star-Lord", "team": "Guardians", "power": 70},
    {"name": "Gamora", "team": "Guardians", "power": 80},
    {"name": "Wolverine", "team": "X-Men", "power": 90},
    {"name": "Storm", "team": "X-Men", "power": 85}
]

# Filter Avengers
avengers = list(filter(lambda h: h["team"] == "Avengers", heroes))

# Map to get names of powerful heroes
powerful_heroes = list(map(lambda h: h["name"], 
                           filter(lambda h: h["power"] >= 85, heroes)))

print("Avengers:", [hero["name"] for hero in avengers])
print("Powerful heroes:", powerful_heroes)

# Combine filtering and mapping in a list comprehension
powerful_non_avengers = [h["name"] for h in heroes if h["power"] >= 80 and h["team"] != "Avengers"]
print("Powerful non-Avengers:", powerful_non_avengers)

# This shows advanced list operations using filter(), map(), and list comprehensions.

# MARKDOWN CELL
## Very Advanced Example

# MARKDOWN CELL
### 1. Multidimensional Lists with Sci-Fi Multiverse

# CODE CELL
import random

# Create a multidimensional list representing a sci-fi multiverse
class SciFiMultiverse:
    def __init__(self, dimensions, universes_per_dimension):
        self.multiverse = [
            [
                [
                    {"id": f"D{d}U{u}P{p}", 
                     "technology": random.randint(1, 100),
                     "magic": random.randint(1, 100),
                     "aliens": random.choice([True, False])}
                    for p in range(5)  # 5 planets per universe
                ]
                for u in range(universes_per_dimension)
            ]
            for d in range(dimensions)
        ]

    def get_universe(self, dimension, universe):
        return self.multiverse[dimension][universe]

    def get_planet(self, dimension, universe, planet):
        return self.multiverse[dimension][universe][planet]

    def find_habitable_planets(self, min_tech, min_magic):
        habitable = []
        for d, dimension in enumerate(self.multiverse):
            for u, universe in enumerate(dimension):
                for p, planet in enumerate(universe):
                    if planet["technology"] >= min_tech and planet["magic"] >= min_magic:
                        habitable.append((d, u, p, planet))
        return habitable

    def alien_invasion(self, dimension, universe):
        for planet in self.multiverse[dimension][universe]:
            if planet["aliens"]:
                planet["technology"] += 10
                print(f"Alien invasion on {planet['id']}! Technology increased.")
            else:
                planet["magic"] += 5
                print(f"Magical surge on {planet['id']}! Magic increased.")

# Use the SciFiMultiverse
multiverse = SciFiMultiverse(dimensions=3, universes_per_dimension=2)

# Find habitable planets
habitable_planets = multiverse.find_habitable_planets(min_tech=70, min_magic=70)
print("Habitable planets:")
for dimension, universe, planet, data in habitable_planets:
    print(f"Planet {data['id']}: Tech = {data['technology']}, Magic = {data['magic']}, Aliens = {data['aliens']}")

# Simulate an alien invasion
print("\nAlien Invasion in Dimension 1, Universe 0:")
multiverse.alien_invasion(1, 0)

# Check the affected universe after the invasion
affected_universe = multiverse.get_universe(1, 0)
print("\nAffected Universe after invasion:")
for planet in affected_universe:
    print(f"Planet {planet['id']}: Tech = {planet['technology']}, Magic = {planet['magic']}, Aliens = {planet['aliens']}")

# This very advanced example uses multidimensional lists to represent a complex sci-fi multiverse,
# demonstrating nested list creation, accessing, and manipulation.

# MARKDOWN CELL
# Congratulations! You've explored Python lists from simple operations to advanced multidimensional structures.
# Keep experimenting and may your lists always be filled with exciting adventures!