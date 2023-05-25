# 1. referring to a function by a variable name

def greet():
    a = 1
    b = 2
    return'hello', a+b

# assigning the function greet to the new variable hello
"""print(greet)
print(greet())"""
hello1 = greet # Type: function
hello2 = greet()# Type tuple
"""print(type(hello1))
print(type(hello2))"""
# hello()


### pass functions as input arguments to other functions

def add_numbers(a,b):
    return a+b

def mult_numbers(a,b):
    return a*b

def math_operation(func, x, y):
    result = func(x, y)
    return result

result_add = math_operation(add_numbers, 2, 3)
result_mult = math_operation(mult_numbers, 2, 3)
print(result_add)
print(result_mult)


# return functions as output from a function

def math_operation(operation):
    if operation == 'add':
        return add_numbers
    elif operation == 'mult':
        return mult_numbers
    return None

"""print(add_numbers) #
print(add_numbers(1,2)) # prints integer"""

result_add = math_operation('add')
print(result_add(1,2))

result_add_func = math_operation('add')
"""print(type(result_add_func))
print(result_add_func(1,2))"""

result_add = math_operation('add')(1,2)
print(result_add)

##### Closures

def make_averager():
    series = []
    
    """def averager(new_value):
        pass"""
    def averager(new_value):
        series.append(new_value)
        print(series)
        total = sum(series)
        return total/len(series)
    print('OUTER', series)
     
    
    def my_sum(new_value):
        return sum(series)
    return averager, my_sum
print(make_averager()[0](10))

"""avg = make_averager() 
print(avg)
print(avg(10))
print(avg(1))"""

##### Closures ######

def make_averager():
    series = [] ### free variable

    def averager(new_value):
        series.append(new_value)
        print(series)
        total = sum(series)
        return total/len(series)
    
    def my_sum(new_value):
        return sum(series)

    return averager, my_sum

print(make_averager()[0](10))

def outer_function(my_parameter1):

    def print_parameter1(value1):
        print(my_parameter1)
        print(value1)
        return value1

        #def most_inner(value2):
         #   print(my_parameter1) # free variable
         #   print(value1) # free variable
         #   print(value2) # local variable

        #return most_inner    

    return print_parameter1

inner_func = outer_function('BLA') # function
inner_func('Hello world')

#outer_function('BLA')('')('again')

print(type(outer_function('BLA')))
print(type(outer_function('BLA')(100)))

### Packing, unpacking, *args, **kwargs

##### closure II ###

series = [] # global variable

def make_averager():
    series = [] # local variable for make_averager
    
    def averager(new_value):
        series.append(new_value) # series is a free variable
        total = sum(series)
        return total/len(series)
    
    return averager

avg = make_averager()

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

 ### ####

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager

avg = make_averager()
print(avg(10))
print(avg(1))

## Implementing a Simple Decorator
"""import time
def snooze(s):
    print(f"{s} seconds to sleep")
    time.sleep(s)
    print('bla')
    return 'Wake up'

snooze(2)    """

"""def clock(fun):
    def clocked(bla):
        t0 = time.time()
        result = fun(bla)
        elapsed = time.time() - t0
        print(f'It took {elapsed} s.')
        return result + ' Bob'
    return clocked

snooze = clock(snooze)
print(snooze(1))
"""

"""def clock(fun):
    def clocked(bla):
        start_time = time.time()
        print(start_time)
        result = fun(bla)
        end_time = time.time()
        elapsed = time.time() - start_time
        print(f'It took {elapsed} s.')
        return result + ' Bob'
    return clocked

snooze = clock(snooze)
print(snooze(1))"""

#####
import time

def clock(fun):
    def clocked(bla):
        start_time = time.time()
        print('TIME START', start_time)
        result = fun(bla)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f'It took {elapsed} s.')
        return result + ' Bob'
    return clocked

def snooze(s):
    print(s)
    time.sleep(s)
    print('bla')
    return 'Wack up'

snooze1 = clock(snooze)
snooze1(1)

@clock
def snooze(s):
    print(s)
    time.sleep(s)
    print('bla')
    return 'Wake up'
snooze(1)

def fac(n): # 1 * 2 * 3 * ...* n
    result = 1
    while n>=1 :
        result = result * n
        n -= 1
        return result
    print(fac(10))

# print(fac(10))


def decorator(func):
    def inner(*args, **kwargs):
        return 'deco ' + func(*args, **kwargs)
    return inner

decorator
def test(w1, w2='world'):
    return f'{w1} {w2}'
test = decorator(test)

print(test('Hello'))

########################################
def make_bold(func):
    def inner():
        return f"<strong> {func()} </strong>"
    return inner

def get_html_greetings():
    return f"Hello world"

get_html_greetings = make_bold(get_html_greetings) # Tyoe Function
print(get_html_greetings())


def wrap_with(tag='div'):
    def decorator(func):
        def inner():
            return f"<{tag}> {func()}</{tag}>"
        return inner
    return decorator

def test(w1, w2='world'):
         return f'Hello world'

test = wrap_with(tag='strong')(get_html_greetings)
print(test())


@wrap_with('strong')
def get_html_greetings():
    return f"Hello world"

print(get_html_greetings())
