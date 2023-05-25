"""Exercise (closure II):

create a function double analogous to the triple triple
what is the free variable?
what is the closure?
use code.co_varnames, code.co_freevars, and closure[0].cell_contents"""

# Solution

# Define the double function
def double():
    a = 2  # Define the local variable 'a' with a value of 2
    
    # Define the nested function multiply
    def multiply(b):
        return a * b  # Access the free variable 'a' from the enclosing scope and multiply it with 'b'
    
    return multiply  # Return the multiply function as the result of double()

# Call the double function and immediately call the returned function with an argument
inner = double()

# Use introspection to check the details

# Print the local variable names in the multiply function
print(inner.__code__.co_varnames)  # Output: ('b',)

# Print the free variable names in the multiply function
print(inner.__code__.co_freevars)  # Output: ('a',)

# Access the value of the free variable 'a' through the closure
print(inner.__closure__[0].cell_contents)  # Output: 2
