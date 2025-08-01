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
l1 = [1,2,3,4]
l2 = l1
print(l2)
l2[0] = 55
print(l2)
print(l1)
#  In Python, variables don’t store data directly, they store a reference (a pointer) to an object in memory.