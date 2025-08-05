# Function with default parameter
def default_parameter(city='Lahore'):
    print(city, 'is Your city')

default_parameter('Okara')


# Function with unknown number of positional arguments (*args)
def unknown_parameters(*name):
    print('The name of the winner is', name[1])

unknown_parameters('Ali', 'Haider', 'Hafiz')


# Function with keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is", child1)

my_function(child1="Emil", child2="Tobias", child3="Linus")


# Passing a dictionary to a function
students = {
    'name': 'Ali',
    'age': 21,
}

def passing_dict(info):
    for key in info:
        print(key, ':', info[key])

passing_dict(students)


# Basic function returning square
def square(number):
    return number ** 2

print(square(9))


# Function for multiplication
def multiply(q, w):
    return q * w

print(multiply(8, 2))
print(multiply('a', 2))
print(multiply(2, 'a'))


# Function to calculate area and circumference of a circle
import math

def circle(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle(3)
print('Area:', round(a, 2), 'Circumference:', round(c, 2))


# Function with default greeting
def default_greeting(greet='Good morning'):
    print('Hey Sir!', greet)

default_greeting()


# Lambda function (anonymous function)
cube = lambda x: x ** 3
print(cube(2))


# Sum using *args
def sum_all(*args):
    return sum(args)

print(sum_all(2, 4, 5, 2))


# Function with keyword arguments (**kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='Ali', age=21, power='Lazer')


# Generator function using yield
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)


# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
