"""Exercise 3 (Decorators - uppercase):
Create a decorator named uppercase that converts the result of a function to uppercase. Use this decorator to decorate the function get_message that returns a string message.
def uppercase(func):
.......
......

.........
def get_message():
return "Welcome to Python!"

message = get_message()
print(message) # WELCOME TO PYTHON!"""

# Solution

def uppercase(func):
    # This is the decorator function
    def wrapper():
        # This is the wrapper function that calls the original function
        result = func()  # Call the original function and store the result
        return result.upper()  # Convert the result to uppercase and return it
    return wrapper

@uppercase
def get_message():
    # Original function that returns a string message
    return "Welcome to Python!"

message = get_message()
print(message)  # Print the converted message

print("___________________________________________")

# Solution 2
class UppercaseDecorator:
    def __init__(self, func):
        # Initialize the decorator with the original function
        self.func = func

    def __call__(self, *args, **kwargs):
        # This method allows instances of the class to be called as functions
        result = self.func(*args, **kwargs)  # Call the original function with arguments
        return result.upper()  # Convert the result to uppercase and return it

@UppercaseDecorator
def get_message():
    # Original function that returns a string message
    return "Welcome to Python!"

message = get_message()
print(message)  # Print the converted message
