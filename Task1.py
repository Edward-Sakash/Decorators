"""Exercise (closure I):
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
use inner.__ code__.co_varnames and inner. code__.co_freevars, and inner.__ closure__[0].cell_contents  to double check. (edited) 
New
3:15
Exercise (closure II):"""

# Solution
# Define the triple function
def triple():
    a = 3  # Define the local variable 'a' with a value of 3
    
    # Define the nested function multiply
    def multiply(b):
        return a * b  # Access the free variable 'a' from the enclosing scope and multiply it with 'b'
    
    return multiply  # Return the multiply function as the result of triple()

# Call the triple function and immediately call the returned function with an argument of 6
triple()(6)

# Assign the triple function to the variable 'inner'
inner = triple()

# Use introspection to check the details

# Print the local variable names in the multiply function
print(inner.__code__.co_varnames)  # Output: ('b',)

# Print the free variable names in the multiply function
print(inner.__code__.co_freevars)  # Output: ('a',)

# Access the value of the free variable 'a' through the closure
print(inner.__closure__[0].cell_contents)  # Output: 3
