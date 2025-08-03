# Tuple is similar to List, but the difference is that Tuples are immutable (cannot be changed)
my_tuple = ('Ali', 21, True)  # simple tuple
print(my_tuple)

print(my_tuple[1])  # it will give the value at index 1
print(my_tuple[0])  # it will give the value at index 0

# Looping over a tuple
for item in my_tuple:
    print(item)

# Convert tuple to list
new_list = list(my_tuple)
print(new_list)

# Convert list back to tuple
new_tuple = tuple(new_list)
print(new_tuple)

# Tuple slicing
print(new_tuple[0:1])
print(new_tuple[1:])

# Tuple concatenation
car_tuple = ('Honda', 'Kia', 'BMW', 'BMW', 'GMC')
all_tuple = car_tuple + new_tuple
print(all_tuple)

# Conditional check in tuple
if 'Honda' in all_tuple:
    print('Yes, Honda is present')

# Count method in tuple
print(all_tuple.count('BMW'))  # how many times 'BMW' appears

# Tuple unpacking
color = ('red', 'green', 'black')
(red, green, black) = color
print(red)

# Nested tuple access
nested_tuple = (
    'red',
    'green',
    ('red', ('red', 'green', 'black'), 'green', 'black'),
    'black'
)
print(nested_tuple[2][1][0])  # Accessing nested tuple value
