#  DESCRIPTION Learn Python's sorted() function through pop culture examples, from simple to advanced levels.

# MARKDOWN CELL
# Python sorted() Function: From Simple to Advanced

# Let's dive into Python's sorted() function with fun examples inspired by pop culture, music, movies, and more!

# MARKDOWN CELL
## Very Simple Examples

# MARKDOWN CELL
### 1. Sorting Hogwarts Houses

# CODE CELL
# Sort Hogwarts houses alphabetically
hogwarts_houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
sorted_houses = sorted(hogwarts_houses)

print("Original order:", hogwarts_houses)
print("Sorted order:", sorted_houses)

# This example demonstrates basic sorting of strings.
# The sorted() function returns a new sorted list, leaving the original list unchanged.

# MARKDOWN CELL
### 2. Ranking Superhero Powers

# CODE CELL
# Sort superheroes by their power level
power_levels = [85, 100, 92, 78, 95]
sorted_powers = sorted(power_levels, reverse=True)

print("Original power levels:", power_levels)
print("Sorted power levels (highest to lowest):", sorted_powers)

# Here we sort numbers in descending order using the 'reverse' parameter.
# This is useful for creating rankings or leaderboards.

# MARKDOWN CELL
### 3. Organizing Pokémon by Name Length

# CODE CELL
# Sort Pokémon names by their length
pokemon = ["Pikachu", "Charizard", "Mew", "Gyarados", "Snorlax"]
sorted_pokemon = sorted(pokemon, key=len)

print("Original Pokémon list:", pokemon)
print("Sorted by name length:", sorted_pokemon)

# This example introduces the 'key' parameter, using the len function.
# It sorts the list based on the length of each string.

# MARKDOWN CELL
## Simple Examples

# MARKDOWN CELL
### 1. Sorting Star Wars Episodes

# CODE CELL
# Sort Star Wars movies by episode number
star_wars_movies = [
    ("The Phantom Menace", 1),
    ("A New Hope", 4),
    ("The Empire Strikes Back", 5),
    ("Attack of the Clones", 2),
    ("Return of the Jedi", 6),
    ("Revenge of the Sith", 3)
]

sorted_movies = sorted(star_wars_movies, key=lambda x: x[1])

print("Sorted Star Wars movies:")
for movie, episode in sorted_movies:
    print(f"Episode {episode}: {movie}")

# This example sorts a list of tuples based on the episode number.
# We use a lambda function as the 'key' to specify which element to sort by.

# MARKDOWN CELL
### 2. Ranking Marvel Superheroes

# CODE CELL
# Rank Marvel superheroes by power level
heroes = [
    {"name": "Iron Man", "power": 85},
    {"name": "Thor", "power": 95},
    {"name": "Black Widow", "power": 75},
    {"name": "Hulk", "power": 92},
    {"name": "Captain America", "power": 88}
]

sorted_heroes = sorted(heroes, key=lambda x: x["power"], reverse=True)

print("Ranked Marvel Superheroes:")
for hero in sorted_heroes:
    print(f"{hero['name']}: Power level {hero['power']}")

# Here we sort a list of dictionaries based on the 'power' key.
# The lambda function extracts the 'power' value for sorting.

# MARKDOWN CELL
### 3. Sorting Harry Potter Spells

# CODE CELL
# Sort Harry Potter spells by name and difficulty
spells = [
    ("Expelliarmus", 3),
    ("Lumos", 1),
    ("Avada Kedavra", 5),
    ("Wingardium Leviosa", 2),
    ("Accio", 3)
]

sorted_spells = sorted(spells, key=lambda x: (x[1], x[0]))

print("Sorted Harry Potter Spells (by difficulty, then alphabetically):")
for spell, difficulty in sorted_spells:
    print(f"{spell} - Difficulty: {difficulty}")

# This example demonstrates sorting with multiple criteria.
# We sort first by difficulty, then alphabetically by spell name.

# MARKDOWN CELL
## Intermediate Examples

# MARKDOWN CELL
### 1. Sorting Lord of the Rings Characters

# CODE CELL
from operator import itemgetter

# Sort LOTR characters by race and then age
characters = [
    ("Frodo", "Hobbit", 50),
    ("Aragorn", "Man", 87),
    ("Legolas", "Elf", 2931),
    ("Gimli", "Dwarf", 139),
    ("Pippin", "Hobbit", 28),
    ("Boromir", "Man", 41)
]

sorted_characters = sorted(characters, key=itemgetter(1, 2))

print("Sorted Lord of the Rings Characters:")
for name, race, age in sorted_characters:
    print(f"{name}: {race}, {age} years old")

# This example introduces the itemgetter function for more efficient sorting.
# We sort first by race, then by age within each race.

# MARKDOWN CELL
### 2. Organizing a Spotify Playlist

# CODE CELL
from datetime import datetime

# Sort a Spotify playlist by release year and song length
playlist = [
    {"title": "Bohemian Rhapsody", "artist": "Queen", "year": 1975, "length": 355},
    {"title": "Billie Jean", "artist": "Michael Jackson", "year": 1983, "length": 294},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "year": 1991, "length": 301},
    {"title": "Like a Rolling Stone", "artist": "Bob Dylan", "year": 1965, "length": 373},
    {"title": "Purple Rain", "artist": "Prince", "year": 1984, "length": 520}
]

sorted_playlist = sorted(playlist, key=lambda x: (x["year"], x["length"]))

print("Sorted Spotify Playlist:")
for song in sorted_playlist:
    length = datetime.utcfromtimestamp(song["length"]).strftime("%M:%S")
    print(f"{song['title']} by {song['artist']} ({song['year']}) - {length}")

# This example sorts a list of dictionaries by multiple criteria.
# We sort first by release year, then by song length.
# We also demonstrate formatting the song length as minutes:seconds.

# MARKDOWN CELL
### 3. Ranking Sci-Fi Franchises

# CODE CELL
# Rank sci-fi franchises by fan rating and box office earnings
franchises = [
    ("Star Wars", 4.8, 10000),
    ("Star Trek", 4.5, 8000),
    ("Doctor Who", 4.6, 6000),
    ("Battlestar Galactica", 4.7, 5000),
    ("The Matrix", 4.4, 7000)
]

# Custom sorting function
def franchise_rank(franchise):
    name, rating, earnings = franchise
    return (-rating, -earnings)  # Negative for descending order

sorted_franchises = sorted(franchises, key=franchise_rank)

print("Ranked Sci-Fi Franchises:")
for i, (name, rating, earnings) in enumerate(sorted_franchises, 1):
    print(f"{i}. {name} - Rating: {rating}, Box Office: ${earnings}M")

# This example uses a custom function for complex sorting criteria.
# We rank franchises first by rating, then by earnings, both in descending order.

# MARKDOWN CELL
## Advanced Examples

# MARKDOWN CELL
### 1. Sorting Marvel Characters by Multiple Attributes

# CODE CELL
from operator import attrgetter
from collections import namedtuple

# Define a namedtuple for Marvel characters
Character = namedtuple('Character', ['name', 'alter_ego', 'power_level', 'intelligence', 'speed'])

# Create a list of Marvel characters
marvel_characters = [
    Character("Spider-Man", "Peter Parker", 85, 95, 90),
    Character("Iron Man", "Tony Stark", 80, 100, 70),
    Character("Black Widow", "Natasha Romanoff", 75, 90, 85),
    Character("Thor", "Thor Odinson", 95, 80, 88),
    Character("Captain America", "Steve Rogers", 88, 85, 87)
]

# Sort characters by power level (descending), then intelligence, then speed
sorted_characters = sorted(marvel_characters, 
                           key=attrgetter('power_level', 'intelligence', 'speed'), 
                           reverse=True)

print("Sorted Marvel Characters:")
for char in sorted_characters:
    print(f"{char.name} (Alter Ego: {char.alter_ego}):")
    print(f"  Power Level: {char.power_level}")
    print(f"  Intelligence: {char.intelligence}")
    print(f"  Speed: {char.speed}")
    print()

# This advanced example uses namedtuples and the attrgetter function.
# We sort by multiple attributes in a specific order of priority.

# MARKDOWN CELL
### 2. Time Lord Regeneration Sorter

# CODE CELL
import re
from datetime import datetime

# Sort Doctor Who incarnations by era and regeneration energy
doctors = [
    "Thirteenth Doctor (Jodie Whittaker) - 2017 - Energy: 89%",
    "First Doctor (William Hartnell) - 1963 - Energy: 95%",
    "Tenth Doctor (David Tennant) - 2005 - Energy: 92%",
    "Fourth Doctor (Tom Baker) - 1974 - Energy: 88%",
    "War Doctor (John Hurt) - 2013 - Energy: 97%"
]

def extract_info(doctor_string):
    match = re.match(r"(\w+) Doctor .* - (\d{4}) - Energy: (\d+)%", doctor_string)
    if match:
        ordinal, year, energy = match.groups()
        return (datetime.strptime(year, "%Y"), 
                ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth", "Thirteenth"].index(ordinal), 
                int(energy))
    return (datetime.min, -1, 0)

sorted_doctors = sorted(doctors, key=extract_info)

print("Sorted Doctor Who Incarnations:")
for doctor in sorted_doctors:
    print(doctor)

# This advanced example uses regular expressions and custom sorting logic.
# We extract information from strings and sort based on multiple criteria.

# MARKDOWN CELL
### 3. Multiversal Rick Sorter

# CODE CELL
import random

# Generate and sort Ricks from different dimensions in Rick and Morty
dimensions = ["C-137", "J19ζ7", "35-C", "K-83", "D-99", "Pizza"]
attributes = ["intelligence", "morality", "alcoholism", "scientific_knowledge"]

def generate_rick(dimension):
    return {
        "dimension": dimension,
        "intelligence": random.randint(60, 100),
        "morality": random.randint(0, 100),
        "alcoholism": random.randint(50, 100),
        "scientific_knowledge": random.randint(70, 100)
    }

ricks = [generate_rick(dim) for dim in dimensions]

def rick_sort_key(rick):
    return (
        -rick["intelligence"],
        -rick["scientific_knowledge"],
        rick["morality"],
        -rick["alcoholism"]
    )

sorted_ricks = sorted(ricks, key=rick_sort_key)

print("Sorted Multiverse Ricks:")
for rick in sorted_ricks:
    print(f"Rick from Dimension {rick['dimension']}:")
    for attr in attributes:
        print(f"  {attr.capitalize()}: {rick[attr]}")
    print()

# This advanced example generates random data and uses a complex sorting function.
# We sort Ricks based on multiple attributes with different priorities and directions.

# MARKDOWN CELL
## Very Advanced Example

# MARKDOWN CELL
### 1. Infinity Stone Power Balancer

# CODE CELL
import random
from functools import cmp_to_key

# Simulate balancing the power of the Infinity Stones
stones = ["Space", "Reality", "Power", "Mind", "Time", "Soul"]

class InfinityStone:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(80, 100)
        self.instability = random.randint(1, 20)
        self.synergy = {stone: random.randint(1, 10) for stone in stones if stone != name}

    def __repr__(self):
        return f"{self.name} Stone (Power: {self.power}, Instability: {self.instability})"

def stone_power_balance(stone1, stone2):
    # Complex comparison logic
    power_diff = stone2.power - stone1.power
    instability_diff = stone1.instability - stone2.instability
    synergy_diff = sum(stone2.synergy.values()) - sum(stone1.synergy.values())
    
    total_diff = power_diff + instability_diff + synergy_diff
    
    if abs(total_diff) < 5:  # Stones are relatively balanced
        return random.choice([-1, 1])  # Random tiebreaker
    return total_diff

# Create Infinity Stones
infinity_stones = [InfinityStone(name) for name in stones]

# Sort stones based on the complex balance function
balanced_stones = sorted(infinity_stones, key=cmp_to_key(stone_power_balance))

print("Balanced Infinity Stones:")
for stone in balanced_stones:
    print(stone)
    print(f"  Synergies: {stone.synergy}")
    print()

# Calculate total power of the Infinity Gauntlet
total_power = sum(stone.power for stone in balanced_stones)
total_instability = sum(stone.instability for stone in balanced_stones)
total_synergy = sum(sum(stone.synergy.values()) for stone in balanced_stones)

print(f"Infinity Gauntlet Stats:")
print(f"Total Power: {total_power}")
print(f"Total Instability: {total_instability}")
print(f"Total Synergy: {total_synergy}")
print(f"Balance Factor: {total_power + total_synergy - total_instability}")

# This very advanced example uses custom classes, complex comparison logic, and the cmp_to_key function.
# We simulate balancing the Infinity Stones based on multiple interrelated factors.

# MARKDOWN CELL
# Congratulations! You've mastered Python's sorted() function across various complexity levels.
# Keep exploring and may your code always be perfectly sorted!