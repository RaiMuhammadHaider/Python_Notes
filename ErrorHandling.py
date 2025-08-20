x = ('mango', 'orange' , 'banana')
y = enumerate(x)
print(y)
print(list(y))
# this is our first method 
# myFile = open('myfile.py', 'w')
# with open('myfile.py','w') as myfile:
#     myfile.write('this is my file')
with open('Second.py','w') as secnod: # it will create or open a file that we fill in it enter the name of the file 
    secnod.write('hey! i am Second File')  # it will make changes of the file 
# and this one is our second method 
apniFile = open('Apni.py','w')
try:
    apniFile.write('ya to ha apni file')
finally:
    apniFile.close()