# MARKDOWN CELL
# # Lambda Function Exercises
# 
# This notebook contains exercises to practice lambda functions in Python, ranging from simple to very advanced levels.

# MARKDOWN CELL
# ## Simple Examples

# CODE CELL
# DESCRIPTION: Simple lambda function examples

# Example 1: Square a number
square = lambda x: x**2
print(square(5))  # Output: 25

# Example 2: Add two numbers
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

# Example 3: Check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True
print(is_even(7))  # Output: False

# MARKDOWN CELL
# ## Intermediate Examples

# CODE CELL
# DESCRIPTION: Intermediate lambda function examples

# Example 1: Sort a list of tuples based on the second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Example 2: Filter out odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example 3: Map a list of temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# MARKDOWN CELL
# ## Advanced Examples

# CODE CELL
# DESCRIPTION: Advanced lambda function examples

from functools import reduce

# Example 1: Use reduce with a lambda function to find the product of a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Example 2: Create a closure with a lambda function
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# Example 3: Use a lambda function with sorted() and a custom key
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

# MARKDOWN CELL
# ## Very Advanced Examples

# CODE CELL
# DESCRIPTION: Very advanced lambda function examples

import operator

# Example 1: Create a simple calculator using a dictionary of lambda functions
calc = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

print(calc['+'](5, 3))  # Output: 8
print(calc['*'](4, 7))  # Output: 28

# Example 2: Implement a basic currying function using lambda
def curry(func):
    return lambda x: lambda y: func(x, y)

add = curry(operator.add)
add_five = add(5)
print(add_five(3))  # Output: 8

# Example 3: Create a decorator using lambda functions
def debug(func):
    return lambda *args, **kwargs: print(f"Calling {func.__name__}") or func(*args, **kwargs)

@debug
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Calling greet \n Hello, Alice!