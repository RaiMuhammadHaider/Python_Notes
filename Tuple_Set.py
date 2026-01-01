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

#memebership testing 
print(f"check it available or not: {"red" in nested_tuple}") # it will show in boolean

# Set 

any_set_A = {"ali" , 'Haider' ,2,4,5,6,7}
any_set_B = {"ali" , "car" ,  0 ,8,7,6,5}
Set_C = any_set_A | any_set_B # this will make it union all will come in orfer
print(f"set : {Set_C}")
set_D = any_set_A & any_set_B
print(f"set : {set_D}") # only common will come 
set_F = any_set_A - any_set_B # neglect B from A
print(set_F)