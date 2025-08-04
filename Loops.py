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

#  Retry system with exponential wait
import time
wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print('Attempt', attempts + 1, '- wait time', wait_time, 'seconds')
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
