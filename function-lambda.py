#  DESCRIPTION: Explore Python lambda functions with pop culture references, from simple to advanced levels.

# MARKDOWN CELL
# Python Lambda Functions: From Novice to Jedi Master

# In this notebook, we'll explore Python lambda functions at various complexity levels, using fun examples inspired by pop culture, music, movies, food, travel, science, and space. Let's dive in!

# MARKDOWN CELL
# Very Simple Examples

# These examples demonstrate the basic syntax and usage of lambda functions.

# CODE CELL
# Example 1: Squaring numbers
#  DESCRIPTION: Simple lambda to square a number, inspired by Super Mario's power-ups.
square = lambda x: x ** 2
print(f"Mario's power level: {square(3)}")  # Output: 9

# Example 2: Greeting function
#  DESCRIPTION: Lambda to create a simple greeting, inspired by E.T.
greet = lambda name: f"E.T. says: Hello, {name}!"
print(greet("Elliott"))  # Output: E.T. says: Hello, Elliott!

# Example 3: Check if a number is even
#  DESCRIPTION: Lambda to determine if a number is even, using a Stranger Things reference.
is_even = lambda x: x % 2 == 0
print(f"Is Eleven even? {is_even(11)}")  # Output: False

# MARKDOWN CELL
# Simple Examples

# These examples show how lambda functions can be used with built-in functions.

# CODE CELL
# Example 1: Sorting a list of tuples
#  DESCRIPTION: Sort a list of movie tuples by release year using a lambda function.
movies = [("Back to the Future", 1985), ("Jurassic Park", 1993), ("The Matrix", 1999)]
sorted_movies = sorted(movies, key=lambda movie: movie[1])
print("Sorted movies:", sorted_movies)

# Example 2: Filtering a list
#  DESCRIPTION: Filter a list of numbers to keep only those divisible by 3, inspired by "The Rule of Three" in storytelling.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))
print("Numbers divisible by three:", divisible_by_three)

# Example 3: Mapping temperature conversion
#  DESCRIPTION: Convert a list of Celsius temperatures to Fahrenheit using a lambda function.
celsius_temps = [0, 15, 30, 45]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print("Fahrenheit temperatures:", fahrenheit_temps)

# MARKDOWN CELL
# Intermediate Examples

# These examples demonstrate more complex uses of lambda functions.

# CODE CELL
# Example 1: Custom sorting with multiple criteria
#  DESCRIPTION: Sort a list of dictionaries by multiple keys using a lambda function.
songs = [
    {"title": "Bohemian Rhapsody", "artist": "Queen", "year": 1975},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "year": 1991},
    {"title": "Like a Prayer", "artist": "Madonna", "year": 1989}
]
sorted_songs = sorted(songs, key=lambda song: (song["year"], song["title"]))
print("Sorted songs:", sorted_songs)

# Example 2: Partial function application
#  DESCRIPTION: Create a partial function for calculating discounted prices, inspired by arcade game pricing.
from functools import partial

apply_discount = lambda price, discount: price * (1 - discount)
twenty_percent_off = partial(apply_discount, discount=0.2)
print(f"Discounted game price: ${twenty_percent_off(50):.2f}")

# Example 3: Nested lambda functions
#  DESCRIPTION: Create a function that returns a lambda, inspired by inception levels in the movie "Inception".
def create_multiplier(factor):
    return lambda x: x * factor

double = create_multiplier(2)
triple = create_multiplier(3)
print(f"Inception level 2: {double(5)}, level 3: {triple(5)}")

# MARKDOWN CELL
# Advanced Examples

# These examples show more sophisticated uses of lambda functions.

# CODE CELL
# Example 1: Higher-order functions with lambdas
#  DESCRIPTION: Implement a simple function composition using lambda functions, inspired by music mashups.
compose = lambda f, g: lambda x: f(g(x))
to_uppercase = lambda s: s.upper()
add_exclamation = lambda s: s + "!"
shout = compose(add_exclamation, to_uppercase)
print(shout("i love python"))  # Output: I LOVE PYTHON!

# Example 2: Lambda with conditional expressions
#  DESCRIPTION: Use a lambda with a conditional expression to classify planets, inspired by astronomy.
classify_planet = lambda radius, mass: "Gas Giant" if radius > 20000 and mass > 10 else "Terrestrial"
print(f"Earth classification: {classify_planet(6371, 1)}")
print(f"Jupiter classification: {classify_planet(69911, 317.8)}")

# Example 3: Recursive lambda function
#  DESCRIPTION: Create a recursive lambda function to calculate Fibonacci numbers, inspired by the Golden Ratio in nature.
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
print(f"10th Fibonacci number: {fib(10)}")

# MARKDOWN CELL
# Very Advanced Examples

# These examples demonstrate highly sophisticated uses of lambda functions.

# CODE CELL
# Example 1: Y combinator for anonymous recursion
#  DESCRIPTION: Implement the Y combinator to allow recursion in lambda functions, inspired by "Inception" dream levels.
Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
factorial = Y(lambda f: lambda n: 1 if n == 0 else n * f(n-1))
print(f"Factorial of 5: {factorial(5)}")

# Example 2: Currying with lambda functions
#  DESCRIPTION: Implement currying using lambda functions, inspired by multi-step cooking recipes.
curry = lambda f: lambda x: lambda y: lambda z: f(x, y, z)
volume = curry(lambda l, w, h: l * w * h)
print(f"Volume of a 3x4x5 box: {volume(3)(4)(5)}")

# Example 3: Lambda-based mini-language
#  DESCRIPTION: Create a simple symbolic differentiation engine using lambda functions, inspired by sci-fi universal translators.
from operator import add, mul

def deriv(expr):
    if isinstance(expr, (int, float)):
        return lambda x: 0
    elif isinstance(expr, str):
        return lambda x: 1
    elif isinstance(expr, tuple):
        if expr[0] == add:
            return lambda x: deriv(expr[1])(x) + deriv(expr[2])(x)
        elif expr[0] == mul:
            return lambda x: expr[1] * deriv(expr[2])(x) + expr[2] * deriv(expr[1])(x)

expr = (mul, 3, (add, 'x', 5))
derivative = deriv(expr)
print(f"Derivative of 3(x+5) at x=2: {derivative(2)}")