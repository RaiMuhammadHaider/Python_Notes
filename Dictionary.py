# Creating a dictionary
student = {
    'name': 'Ali Haider',
    'age': 21,
    'class': 'BSCS'
}

# Accessing values using keys
print(student)
print(student['name'])  # Access value directly by key
print(student.get('name'))  # Access value safely using get()

# Updating a value
student['age'] = 22
print(student)

# Looping through dictionary keys and values
for key in student:
    print(key, student[key])  # Traditional loop through keys

print('Another method we have:')
for key, value in student.items():  # Recommended way to get both key and value
    print(key, value)

# Checking for key existence
if 'mango' in student:
    print('Yes, the key "mango" is available')  # This will not print, 'mango' not in student

# Dictionary length
print(len(student))  # Total key-value pairs

# Adding a new key-value pair
student['address'] = 'Lahore, Pakistan'
print(student)

# Removing key-value pairs
student.pop('address')  # Remove specific key
print(student)

student.popitem()  # Remove the most recently added key-value pair
print(student)

del student['name']  # Delete a key-value pair using del
print(student)

# Copying a dictionary
college = student.copy()  # Creates a new independent copy
print(college)

# Modifying the copied dictionary
college['location'] = 'Lahore'
print(college)    # New key added in copied dictionary
print(student)    # Original remains unchanged

# Nested dictionary example
Pakistan = {
    'punjab': {
        'kasur': {
            'pattoki': 'Pattoki',
            'habib abad': 'Habib Abad',
            'jambar': 'Jamber'
        },
        'lahore': {
            'kanchi': 'Kanchi',
            'chungi': 'Chungi',
        }
    },
    'sindh': {
        'multan': 'Multan',
        'karachi': 'Karachi'
    }
}

# Accessing nested dictionary values
print(Pakistan['punjab']['lahore']['kanchi'])

# Dictionary comprehension
square_numbers = {x: x**2 for x in range(10)}
print(square_numbers)

# Clearing a dictionary
square_numbers.clear()
print(square_numbers)

# Creating a dictionary using fromkeys()
default_value = 'taste is very good'
dinner = ['tea', 'patato chips', 'burger']
new_dict = dict.fromkeys(dinner, default_value)
print(new_dict)

# Using setdefault() to add a new key with a default value
default = new_dict.setdefault('age', '21')  # Only adds if 'age' doesn't exist
print(new_dict)
