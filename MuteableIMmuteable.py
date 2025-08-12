# if we have created some thing and then if we can change its content is known as mutable in python for example we can change 
# dictionary 
# list
# set  
#  example  for list
fruits = ['apple' , 'Banana' ,'Orange']
print(fruits)
fruits[0] = 'Green Apple' 
# here the value is changed
print(fruits)
print(fruits[0])
#  example for dictionary
student = {
    "name" : 'ali', 
    "age" : 21,
 #in javascript we call it object but in python we call it dictionary make sure the key in double quotes   
}
print(student) 
student['age'] = 100
#  here the dictionary is also changed 
print(student)
#  exampe of set 
our_set = {1,2,3,}
our_set.add(8)
our_set.remove(2)
print(our_set)
# ++++++++++++++++++++++   Immputeable 
#  that never allow to change their content is know is immuteable 
#  int , string , float , toupe 
#  example for string
father_name = 'M Sharif'
print(father_name)
# father_name[0] = 'Muhammad'
print(father_name)
# example for int and float
roll_number = 1393
print(roll_number)
# roll_number[0] = 9999
print(roll_number)
# When you assign a new value to a variable, the variable’s reference is updated to point to the new object.
# If the old object is no longer being used, Python's garbage collector will automatically remove it from memory
x = 10    # here is the x is pointing to a value of 10 in the memory 
y = x     # y have the same reference as the x have
x = 15 # here we have new one value now the new reference 
print(x)
print(y) # but the y still have the old reference

# typecasting #############################
son_name = 'Husnain Bro'
age = 21
married = True
gpa = 3.5
married = int(married)
print(married) # converted into interger which is 1 
son_name = bool(son_name)
print(son_name) # string into boolen true 
age = float(age)
print(age) # converted into float
married = str(married)
print(married) 
print(type(married)) # string 
