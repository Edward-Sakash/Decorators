"""Bonus Exercise:
Create a decorator named logger
 that logs the name of a function before executing it.
 Use this decorator to decorate the function add_numbers
 that takes two numbers as input and returns their sum.
Hint: func.__ name__"""

# Solution
def logger(func):
    # This is the decorator function
    def wrapper(*args, **kwargs):
        # This is the wrapper function that logs the function name and calls the original function
        print(f"Executing function: {func.__name__}")  # Log the name of the function
        return func(*args, **kwargs)  # Call the original function with the given arguments
    return wrapper

@logger
def add_numbers(a, b):
    # Original function that takes two numbers as input and returns their sum
    return a + b

result = add_numbers(3, 5)
print(result)  # Print the result of the function call

print("____________________________________________")

# Solution 2
"""from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # 8"""


from functools import wraps

def logger(func):
    # This is the decorator function
    @wraps(func)
    def wrapper(*args, **kwargs):
        # This is the wrapper function that logs the function name and calls the original function
        print(f"Executing function: {func.__name__}")  # Log the name of the function
        return func(*args, **kwargs)  # Call the original function with the given arguments
    return wrapper

@logger
def add_numbers(a, b):
    # Original function that takes two numbers as input and returns their sum
    return a + b

result = add_numbers(3, 5)
print(result)  # Print the result of the function call

