#  Count total positive numbers
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
number_counter = 0
for num in numbers:
    if num > 0:
        number_counter += 1
print('Total Positive numbers are:', number_counter)

print('-' * 50)

#  Count how many even numbers are up to a given number
number = int(input('Enter any number: '))
even_count = 0
for i in range(0, number + 1):
    if i % 2 == 0:
        even_count += 1
print('Total Even Numbers:', even_count)

print('-' * 50)

#  Multiplication table, skipping 5
number = int(input("Enter the number: "))
for i in range(0, 11):
    if i == 5:
        continue  # Skip 5
    print(number, 'X', i, '=', i * number)

print('-' * 50)

#  Reverse a string
string = 'Haider'
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print('Reversed string:', reversed_string)

print('-' * 50)

#  First non-repeating character
string = 'successfully'
for char in string:
    if string.count(char) == 1:
        print('First non-repeating character:', char)
        break

print('-' * 50)

#  Factorial of a number
number = int(input('Enter number for factorial: '))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print('Factorial value is:', factorial)

print('-' * 50)

#  Ask user to enter number between 1 and 10
while True:
    number = int(input("Enter a number between 1 to 10: "))
    if 1 <= number <= 10:
        print('Thanks')
        break
    else:
        print('Invalid Number, try again.')

print('-' * 50)

#  Check if number is prime
number = int(input("Enter a number to check if prime: "))
if number <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    print('Is Prime:', is_prime)

print('-' * 50)

#  Detect first duplicate in list
items = ['apple', 'orange', 'Banana', 'Kino', 'apple']
seen_items = set()
for item in items:
    if item in seen_items:
        print('Duplicate found:', item)
        break
    seen_items.add(item)

print('-' * 50)

#  Retry system with exponential wait if some one try it will wait again twice
import time
wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print('Attempt', attempts + 1, '- wait time', wait_time, 'seconds')
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1 
####################################         Behind the Seen          #####################################################################
# Topic: Behind the Scene - Iterable, Iterator, Iteration Tool
import time

print('He is my friend')
string = 'haider'
print(string
     # ----------------------------- Explanation -----------------------------

# Iteration tools:
# These are constructs used to perform iteration (looping).
# Examples: for loop, while loop.

# Iterable objects:
# These are objects that can be looped over (i.e., used with iteration tools).
# Examples: list, tuple, string, dictionary, file, set.
# A true iterable must have the __iter__() method defined.

# Iterator:
# An object with a __next__() method, which returns the next item from the iterable.
# You can get an iterator from an iterable by using the iter() function.

# How iteration works (step-by-step):
# 1. When a for loop is run on an iterable object, Python internally calls iter(iterable).
# 2. This returns an iterator object with a __next__() method.
# 3. Python keeps calling next(iterator) to get the next item in the sequence.
# 4. When there are no more items left, a StopIteration exception is raised to end the loop.

# Key Concepts:
# - The iter() function gives an iterator from an iterable object.
# - The next() function fetches the next item from the iterator.
# - Once all items are consumed, next() raises StopIteration.
# - The iterator remembers its current position internally.
# - The memory address of the iterator remains constant, but the pointer moves to the next item.

# Special Note on Files:
# When we open a file using open(), it returns a file object which is also an iterable.
# You can use iter() and next() on it directly to read line-by-line.

# Example:
# my_list = [1, 2, 3]
# iterator = iter(my_list)
# print(next(iterator))  # Output: 1
# print(next(iterator))  # Output: 2
# print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration

# ---------------------------- Notes in Urdu ----------------------------

# Iteration tools wo hoty hain jo iterate karwate hain
# Example: for loop, while loop

# Iterable objects wo hoty hain jin ko hum iterate kar sakte hain
# Example: list, file, dictionary

# Jab hum kisi iterable object ko iterate karte hain, to response milta hai
# Aur ye response deta hai ek iterator object jisme __next__ method hoti hai

# Iterable object memory address return karta hai jahan se iteration start hoti hai

# iter() function iterable object par apply hota hai
# Ye iterable object ko kehta hai: "mujhe iterate karne do"
# Result me ye iterator object return karta hai (with memory address)

# __next__ or next() ka use karke hum agla element get karte hain
# Har bar next() call karne par agla element return hota hai

# Jab sari values iterate ho jati hain, to StopIteration exception raise hoti hai
# Ye indicate karta hai ke aur koi element baqi nahi hai

# Important Point:
# Memory address same rehta hai, lekin pointer agay move karta hai

# File variable jab kisi file ko open karta hai to wo ek iterable object ban jata hai

# Agar hum list ka sirf reference variable banayein (e.g., my_list = [1, 2, 3])
# To wo iterator nahi hota — iterable object hota hai, lekin iterator nahi
# Iterator banane ke liye iter(my_list) use karna padta hai
