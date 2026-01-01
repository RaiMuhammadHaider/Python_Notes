# List basic operations and methods in Python

students = ['Ali', 'Haider', 'Husnain', 'Rai']

print(students[0])  # Access a specific index
print(students)     # Print the whole list
print(len(students))  # Find the length of the list

# Slicing
print(students[:2])  # Show elements from index 0 to 1 (2 not included)
print(students[2:])  # Show elements from index 2 to the end
print(students[:])   # Show all elements

# Replacing part of the list
students[1:2] = ['Rai Muhammad Haider', 'Ali', 'Haider', 'Husnain', 'Rai']
print(len(students))
print(students)

# Iterating over list with custom end character
# for name in students:
#     print(name, end='-')

students.append('Orange')              # Add value at the end
students.pop()                         # Remove the last value
students.remove('Rai Muhammad Haider') # Remove a specific value by name
students.insert(0, 'Inserted value')   # Insert value at a specific index

students.sort()  # Sort list alphabetically or numerically
print(students)

only_reference = students              # Creates a reference (both point to the same list)
New_students = students.copy()         # Creates a separate copy in memory

New_students.insert(0, 'New Student')  # Insert into copied list

print(New_students)  # Both lists are now different
print(students)

# Membership test
if 'Ali' in students:
    print('Yes, Ali is in the list.')

# List comprehension for square numbers
square_number = [x**2 for x in range(10)]
print(square_number)

# List comprehension for cube numbers
cube = [x**3 for x in range(5)]
print(cube)

# List extension and sorting
list1 = [1, 9, 0, 4, 5]
list2 = ['apple', 'orange', 'banana']

# list1.extend(list2)  # Combine list1 and list2 (uncomment to use)
# print(list1)

print(list2)

list2.sort()  # Sort alphabetically (a to z)
print(list2)

list1.sort(reverse=True)  # Sort in descending order
print(list1)

list1.reverse()  # Reverse the list elements
print(list1)

# Using enumerate to get index and value
for index, value in enumerate(list1):
    print(index, value)

print(f"max : {max(list1)}") # for maximum
print(f"min : {min(list1)}") # for minimum
