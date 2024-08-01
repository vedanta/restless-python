#  DESCRIPTION: This program contains a series of exercises to practice lambda functions in Python

# MARKDOWN CELL
# # Lambda Function Exercises
# 
# This notebook contains exercises to practice lambda functions in Python, ranging from simple to very advanced levels. Each example includes detailed explanations to help you understand the concepts better.

# MARKDOWN CELL
# ## Simple Examples

# CODE CELL
# Example 1: Square a number
square = lambda x: x**2
result = square(5)
print(f"The square of 5 is: {result}")  # Output: The square of 5 is: 25

# In this example, we define a lambda function that takes one argument 'x' and returns its square.
# Lambda functions are anonymous functions that can be defined in a single line.
# The syntax is: lambda arguments: expression

# CODE CELL
# Example 2: Add two numbers
add = lambda x, y: x + y
result = add(3, 4)
print(f"3 + 4 = {result}")  # Output: 3 + 4 = 7

# Here, we define a lambda function that takes two arguments 'x' and 'y' and returns their sum.
# This demonstrates that lambda functions can take multiple arguments.

# CODE CELL
# Example 3: Check if a number is even
is_even = lambda x: x % 2 == 0
print(f"Is 6 even? {is_even(6)}")  # Output: Is 6 even? True
print(f"Is 7 even? {is_even(7)}")  # Output: Is 7 even? False

# This lambda function uses the modulo operator (%) to check if a number is even.
# It returns True if the number is even (divisible by 2 with no remainder) and False otherwise.

# MARKDOWN CELL
# ## Intermediate Examples

# CODE CELL
# Example 1: Sort a list of tuples based on the second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"Sorted pairs: {sorted_pairs}")
# Output: Sorted pairs: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Here, we use a lambda function as the 'key' argument in the sorted() function.
# The lambda function returns the second element of each tuple (x[1]), which is used for sorting.
# This demonstrates how lambda functions can be used with built-in functions like sorted().

# CODE CELL
# Example 2: Filter out odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: Even numbers: [2, 4, 6, 8, 10]

# The filter() function applies the lambda function to each element in 'numbers'.
# If the lambda function returns True (i.e., the number is even), the element is included in the result.
# This shows how lambda functions can be used for filtering data.

# CODE CELL
# Example 3: Map a list of temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(f"Fahrenheit temperatures: {fahrenheit}")
# Output: Fahrenheit temperatures: [32.0, 50.0, 68.0, 86.0, 104.0]

# The map() function applies the lambda function to each element in 'celsius'.
# The lambda function converts Celsius to Fahrenheit using the formula (C * 9/5) + 32.
# This demonstrates how lambda functions can be used to transform data.

# MARKDOWN CELL
# ## Advanced Examples

# CODE CELL
# Example 1: Use reduce with a lambda function to find the product of a list
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"The product of {numbers} is: {product}")  # Output: The product of [1, 2, 3, 4, 5] is: 120

# The reduce() function applies the lambda function cumulatively to the items in 'numbers'.
# It multiplies each element with the running product, effectively calculating the product of all numbers.
# This shows how lambda functions can be used with more advanced functional programming concepts.

# CODE CELL
# Example 2: Create a closure with a lambda function
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(f"Double of 5: {double(5)}")  # Output: Double of 5: 10
print(f"Triple of 5: {triple(5)}")  # Output: Triple of 5: 15

# This example demonstrates how lambda functions can be used to create closures.
# The multiplier() function returns a lambda function that remembers the value of 'n'.
# This allows us to create specialized functions like 'double' and 'triple'.

# CODE CELL
# Example 3: Use a lambda function with sorted() and a custom key
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(f"Sorted words: {sorted_words}")  # Output: Sorted words: ['date', 'apple', 'banana', 'cherry']

# This lambda function returns a tuple (len(x), x) for each word.
# The sorted() function uses this tuple to sort the words first by length, then alphabetically.
# This demonstrates how lambda functions can be used to create complex sorting criteria.

# MARKDOWN CELL
# ## Very Advanced Examples

# CODE CELL
# Example 1: Create a simple calculator using a dictionary of lambda functions
calc = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

print(f"5 + 3 = {calc['+'](5, 3)}")  # Output: 5 + 3 = 8
print(f"4 * 7 = {calc['*'](4, 7)}")  # Output: 4 * 7 = 28

# This example uses a dictionary to store lambda functions for basic arithmetic operations.
# The lambda functions are used as values in the dictionary, allowing for dynamic function calls.
# This demonstrates how lambda functions can be used to create flexible, extensible code structures.

# CODE CELL
# Example 2: Implement a basic currying function using lambda
import operator

def curry(func):
    return lambda x: lambda y: func(x, y)

add = curry(operator.add)
add_five = add(5)
result = add_five(3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# This example demonstrates currying, an advanced functional programming technique.
# The curry() function takes a two-argument function and returns a lambda function.
# This lambda function, when called, returns another lambda function, allowing partial application of arguments.

# CODE CELL
# Example 3: Create a decorator using lambda functions
def debug(func):
    return lambda *args, **kwargs: print(f"Calling {func.__name__}") or func(*args, **kwargs)

@debug
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)
# Output:
# Calling greet
# Hello, Alice!

# This example uses a lambda function to create a decorator.
# The debug decorator wraps the original function in a lambda function.
# This lambda function prints a debug message and then calls the original function.
# It demonstrates how lambda functions can be used in metaprogramming techniques like decorators.