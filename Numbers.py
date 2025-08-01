import math
import random
from decimal import Decimal # when we deal with decimal point we import it to get more precise results
persentage = int(2.99992) # int will convert it into integer 
print(persentage)
marks = float(2) # it will convert into flooting points
print(marks)
item = 20 
print (marks + 100 , persentage+3  , item) # we can also get multiple variable values like this
#  Arithematic operators
print ( item / marks)  # for division 
print ( item % marks) # for modulous mean remaing
print ( item * marks) # for multiplication 
print ( item + marks) # for addition 
print ( 25 ** 19 ) # for power 
print('floor Division' , 15 // 2) # it will give the floor value of any divion value mean without decimal value 
#  comparission operators
print(2>5) # 2 is not greater then 5 then it will be false
print(2<5) # as 2 is less then 5 then it will be true
print(2 == 5 ) # as 2 is not equal to 5 then it will also be a false 
print(2 >= 5 ) # greater then or equal then if one of then is true then it will be true
print(2 <= 5 ) # less then or equal then if one of them is true then it will be true
print(2 != 5 ) # is not equal to mean to check it is not equal to yes 2 is not equal to 
#  Logical operators
print( 2 == 2 and 5 ==5 )
number_one = 1
number_two = 2
print( number_one > 4 and number_two < 10 ) # and mean if all are true then it will be true and if one of them is false then the whole will pe false 
print ( number_one > 10 or number_two > 1 ) # if one of them is true then it will be true
print( not(number_one == number_two) ) # not will convert the true into false and false into true mean it will reverse any result
#  Assignment operators
x = 20 
x += 1 # it will be seems like X = X + 1 but mostly expert programmer use it as X += 1
x -= 1 # for substraction
x *= 2 # for multiplication and to assignment to that one value 
x /= 2
x //= 2

print(x)
# Identity operator are use to compare the memory location of two objects . they check the whether two variable refers to the same object in the memory 
t = [1,2,3,4,5]
s = t
print( s is t ) # is will return true if both variables refers to the same object in the memory 
print(id(s))
print(id(t)) # both id's are same mean  both are the same object
t = [1,6,3,0,5]
print(s is t) # it is false because t is now a new object seprate object in the memory
k = [1,6,3,0,5]
print(id(k)) # id will show the object id in the memory 
print(id(t))
#  string 
name = 'ali'
second_name = 'ali'
# name = 'haider' # If multiple variables are assigned the same value (especially of an immutable type like small integers or simple strings), they may refer to the same object in memory. But if any of those variables is later assigned a different value, Python will create a new object in memory for that variable.
print(name is second_name)
boss = [1,2,3,4]
ok_boss = [1,2,3,4]
print(boss is ok_boss) # it is giving false becase the seprate object list is created in the memory
print( boss is not ok_boss) # is not is use to clearify it is not same in object its result is also in boolean form
boss[0] = 55
print(ok_boss is boss) # it is giving as false value because the value of boss list is changed but the ok_boss still have old one 
print(math.floor(3.9)) # floor will give the lower bound value output 3
print(math.floor(-3.9)) # lower value will be -4 
print(math.trunc(3.9)) # it will goes the value towords Zero 0 like in x and y axes it will go to 0
print(math.trunc(-3.9)) # the closest value towords zero is -3
print(int('64', 8)) # converted into octal
print(int('64' , 16)) # it is also converted into hexa 
print( int('10000' , 2)) # it is converted into binary 
# random 
print(random.randint(0,100)) # it will give us random integer according to the range that we have given to it 
juice = ['apple juice', 'mango juice' , 'banana juice', 'orange juice']
print(random.choice(juice)) # it will get random choice that we will provide it it will pick randomlly
random.shuffle(juice)
print(juice)
print(0.1+0.1+0.1-0.3) # this is giving us wrong results that's why we import decimal so library so we can get more accorate results 
print( Decimal("0.1") + Decimal("0.1") - Decimal('0.2')  ) # now it is our accprate result by using the decimal library 
# sets 
set_one = {1,3,7,8}
set_two = {2,4,5,6,9,0}
print(set_two | set_one  ) # this will give us Union all the elements of set into an order
print( set_one & {1,7} ) # this will give us intersection mean common elements of array 
print( set_one - {1,3,7,8}) # it is giving emepty SET() mean nothing the set have it will never ever give empty {} because it is use for only dictionary 

