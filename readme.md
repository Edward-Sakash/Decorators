Exercise 1 (closure I):
- look at the following functions:
def triple():
    a = 3
    def multiply(b):
        return a * b
    return multiply
triple()(6)

inner = triple()
- what is the free variable?
- what is the closure?
use inner.__ code__.co_varnames and inner. code__.co_freevars, and inner.__ closure__[0].cell_contents  to double check.  

Exercise 2 (closure II):
- create a function double analogous to the triple triple
- what is the free variable?
- what is the closure?
- use __code__.co_varnames, __code__.co_freevars, and __closure__[0].cell_contents


Exercise 3 (Decorators - uppercase):
Create a decorator named uppercase that converts the result of a function to uppercase. Use this decorator to decorate the function get_message that returns a string message.
def uppercase(func):
.......
......

.........
def get_message():
    return "Welcome to Python!"

message = get_message()
print(message) # WELCOME TO PYTHON!


Bonus Exercise:
Create a decorator named logger that logs the name of a function before executing it. Use this decorator to decorate the function add_numbers that takes two numbers as input and returns their sum.
Hint: func.__ name__# Decorators
