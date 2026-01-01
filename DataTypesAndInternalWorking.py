# int, float , string , boolean , dictionary , list , nonetpye ,touple , set 
age = 21 # number 
print(type(age))
total_amount = 99.99 # float
print(type(total_amount)) # this will tell us typle of dataType 
name = 'Ali' # string
print(type(name))
is_acrive = False # boolean
print(type(is_acrive))
product = { # dictionary
    'tittle' : 'cosmatic product',
    'price' : 100,
}
print(type(product))
probability_list = ['ali', True , 31] # for list
print(type(probability_list))
result = None  #NoteType none mean empty 
print(type(result))
points = (1,2,3,4) # tuple
print(type(points))
numbers = {1,2,3,4,6} # set
print(type(numbers))


print(len(name)) # this will tell us length 
l1 = [1,2,3,4 , 'orignal']
print(l1)
l2 = l1.copy()  
# By using the .copy() method, we create a new list.
# Now changes will apply only to the copied list, not the original one.

# We can also use l1[:] or list(l1) to create a copy of the list.

# If we do not copy the list and instead write:
# l2 = l1
# then both variables will point to the same object in memory.

l3 = l2
l3[4] = 'now the third one will be copy change'
print(l3)
print(l2)
l2[4] = "Now this is not orignal"
print(l2)


print(l1)
#  In Python, variables don’t store data directly, they store a reference (a pointer) to an object in memory.
# Python uses automatic memory management with reference counting and garbage collection. All objects live in a private heap, and you manipulate references, not raw memory addresses.

chai = set() # set is immoutetable mean there memory address never change 
print(f"this is  : {chai}")
print(f"this is  : {id(chai)}")
chai.add('car')
chai.add('bus')
chai.add('truck') 
print(f"this is  : {id(chai)}")
print(f"this is  : {chai}")

