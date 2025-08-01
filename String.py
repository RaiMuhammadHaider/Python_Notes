# String Operations in Python - Notes by Ali Haider

# Basic string assignment and slicing
name = 'Ali Haider'
print(name)

nam = name[0:4]  # Includes index 0 to 3; does NOT include index 4
print(nam)

ended = name[-1]  # Negative index starts from the end (-1 = last character)
print(ended)

# Slicing a string of digits
number = '0123456789'
print(number[:])        # Prints the whole string
print(number[3:])       # From index 3 to the end
print(number[:3])       # From start to index 2 (3 not included)
print(number[0:9:3])    # From 0 to 9, skipping every 3rd character

# Case conversion
print(name.upper())     # Converts to uppercase
print(name.lower())     # Converts to lowercase

# Trimming and replacing
brother_name = '      Ali    Husnain     '
print(brother_name)
print(brother_name.strip())                    # Removes spaces from both ends
print(brother_name.replace('Ali', 'Okokk'))    # Replaces 'Ali' with 'Okokk'

# String to list
hobbies = 'eating, dancing, planting, drawing'
print(hobbies.split(', '))  # Splits string into list using comma+space

# Finding and counting substrings
print(hobbies.find('dancing'))  # Returns index of 'dancing', -1 if not found
print(len(hobbies))             # Length of string
boss = 'ali haider is my brother brother'
print(boss.count('brother'))    # Counts how many times 'brother' appears

# String formatting
quantity = 2
fruit = 'apple'
order = 'You have ordered {} number of {}'
print(order.format(fruit, quantity))  # Inserts variables into string

# Joining lists into strings
HobbyList = ['drawing', 'boating', 'dancing']
print(' '.join(HobbyList))  # Joins with space
print('-'.join(HobbyList))  # Joins with hyphen (like a URL slug)

# Looping over string
for character in boss:
    print(character)

# Length and escape characters
print(len(boss))
print("He said, \"I am here to help you\"")  # Escape quotes with \"
print(r'user\ali\id')                        # Raw string to print backslashes as-is

# Membership test
print('brother' in boss)  # Checks if 'brother' exists in string (True/False)
