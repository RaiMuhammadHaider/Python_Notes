# Example 1: Timer decorator
import time
def timer(func):  # A decorator that measures how long a function takes to run.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)  # Simulate a slow function

example_function(2)


# Example 2: Simple before/after decorator
def outer(func): #  A decorator that prints a message before and after the function runs.
    def wrapper(*args, **kwargs):
        print('Before')
        func(*args, **kwargs)  # Pass all arguments to the original function
        print('After')
    return wrapper

@outer  # This applies the outer() decorator to hello()
def hello(name):
    print(f"Your name is {name}")

hello('Ali')  # Behind the scenes: hello = outer(hello)


# Example 3: Logging decorator
def decorator(func): # A decorator that logs the function name and all arguments.
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args [{args_value}] and kwargs [{kwargs_value}]")
        func(*args, **kwargs)
    return wrapper

@decorator
def greet(name, greeting='Welcome Sir'):
    print(f"{name}, {greeting}")

greet('Ali', greeting='How are you?')

