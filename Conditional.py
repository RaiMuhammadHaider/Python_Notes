# Check user age group
# user_input = input('Enter your age:\n')  # Get input as string
# user_Age = int(user_input)               # Convert to integer
user_Age = 20  # Example age, replace with input if needed
if user_Age < 13:
    print('Children')
elif user_Age <= 19:
    print('Teenager')
elif user_Age <= 59:
    print('Adult')
else:
    print('Senior')

#########################################################

# Give $2 discount on Wednesday for ticket pricing
age = int(input('Sir, what is your age: '))
day = 'Wednesday'
price = 12 if age >= 18 else 8
if day == 'Wednesday':
    price -= 2
print('Ticket price for you is: $', price)

####################################################################

# Grading system
marks = int(input('Your marks: '))
if marks <= 100:
    if marks >= 90:
        print('A Grade')
    elif marks >= 80:
        print('B Grade')
    elif marks >= 70:
        print('C Grade')
    elif marks >= 60:
        print('D Grade')
    else:
        print('F')
else:
    print('Enter marks between 0 to 100')

#####################################################################

# Banana ripeness check based on color
condition = input('Enter banana color (Green, Yellow, Brown): ')
if condition == 'Green':
    print('Banana is unripe')
elif condition == 'Yellow':
    print('Banana is ripe')
elif condition == 'Brown':
    print('Banana is overripe')
else:
    print('Please enter only Green, Yellow, or Brown')

########################################################################

# Suggest activity based on weather
weather = input('Enter weather (Rainy, Sunny, Snowy): ')
if weather == 'Rainy':
    print('Read a book')
elif weather == 'Sunny':
    print('Go for a walk')
elif weather == 'Snowy':
    print('Build a snowman')
else:
    print('Enter only Rainy, Sunny, or Snowy')

#########################################################

# Transport mode selection based on distance
distance = int(input('Enter the distance (in km): '))
if distance <= 3:
    travel = 'Walk'
elif distance <= 15:
    travel = 'Use Bike'
else:
    travel = 'Use Car'
print(travel)

###########################

# Coffee order with optional extra shot
order_size = 'Medium'
extra_shot = True
if extra_shot:
    coffee = order_size + ' coffee with extra shot'
else:
    coffee = order_size + ' coffee'
print(coffee)

###########################

# Check password strength
password = input('Enter your password: ')
password_length = len(password)
if password_length <= 6:
    check = 'Weak'
elif password_length <= 10:
    check = 'Medium'
else:
    check = 'Strong'
print('Password strength:', check)

###########################

# Check if a year is a leap year
year = int(input('Enter the year: '))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

#######################################

# Suggest food to animals based on age
dog = True
dog_age = 1
cat = True
cat_age = 4

if dog and dog_age <= 2:
    print('Puppy food to dog')
if cat and cat_age <= 5:
    print('Senior food to cat')
