# MARKDOWN CELL
# # Lambda Function Exercises
# 
# Welcome to your daily Python warm-up! Today, we're focusing on lambda functions. These exercises will help you understand and remember how to use lambda functions effectively. Let's dive in!

# CODE CELL
# Simple: Create a lambda function to square a number
square = lambda x: x**2
print(f"The square of 5 is: {square(5)}")

# MARKDOWN CELL
# Great! You've created your first lambda function. Lambda functions are small, anonymous functions that can have any number of arguments but can only have one expression. They're perfect for simple operations.

# CODE CELL
# Intermediate: Use a lambda function with built-in functions like map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")

# MARKDOWN CELL
# In this example, we used a lambda function with `map()` to square each number in a list. This is a common use case for lambda functions.

# CODE CELL
# Advanced: Create a lambda function to sort a list of tuples based on the second element
fruits = [("apple", 5), ("banana", 2), ("cherry", 8), ("date", 1)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print(f"Original fruit list: {fruits}")
print(f"Sorted fruit list: {sorted_fruits}")

# MARKDOWN CELL
# Here, we used a lambda function as the `key` for sorting. This allows us to sort complex data structures based on specific elements.

# CODE CELL
# Very Advanced: Implement a simple calculator using lambda functions and a dictionary
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

def calculator(op, x, y):
    return operations.get(op, lambda: "Invalid operation")(x, y)

print(f"5 + 3 = {calculator('+', 5, 3)}")
print(f"10 - 7 = {calculator('-', 10, 7)}")
print(f"4 * 6 = {calculator('*', 4, 6)}")
print(f"15 / 3 = {calculator('/', 15, 3)}")
print(f"10 / 0 = {calculator('/', 10, 0)}")

# MARKDOWN CELL
# In this advanced example, we created a simple calculator using a dictionary of lambda functions. This demonstrates how lambda functions can be used to create flexible and extensible code.

# CODE CELL
# Fun Exercise: Create a list of your favorite movies and their release years, then sort them by year
movies = [
    ("The Matrix", 1999),
    ("Inception", 2010),
    ("Pulp Fiction", 1994),
    ("The Shawshank Redemption", 1994),
    ("Avengers: Endgame", 2019)
]

sorted_movies = sorted(movies, key=lambda movie: movie[1])
for movie, year in sorted_movies:
    print(f"{movie} was released in {year}")

# MARKDOWN CELL
# This exercise combines what you've learned about lambda functions with a fun, real-world example. You can easily modify this to use your own favorite movies!

# CODE CELL
# Challenge: Create a lambda function to find palindromes in a list of words
words = ["level", "python", "radar", "lambda", "madam", "function"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(f"Original words: {words}")
print(f"Palindromes: {palindromes}")

# MARKDOWN CELL
# In this final challenge, we used a lambda function with `filter()` to find palindromes. The lambda function checks if a word is equal to its reverse.
# 
# Remember to practice these exercises regularly to reinforce your understanding of lambda functions. Happy coding!