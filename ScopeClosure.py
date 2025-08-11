# 🔵 Global Scope Example
globe = ' I am Global Variable'
def outer():
    x = ' I am X (defined in outer)'   
    def inner():
        y = 'I am Y (defined in inner)'
        def most_inner():
            z = '📦 I am Z (defined in most_inner)'
            def last_inner():
                last = ' I am LAST (defined in last_inner)'
                print('--- Inside last_inner ---')
                print(last)
            last_inner()
            print('--- Inside most_inner ---')
            print(globe)  # Accessing global variable
            print(x)      # Accessing from outer
            # print(y)    # Uncomment to access y (from inner)
            # print(z)    # Uncomment to access z (from same function)
        most_inner()
        print('--- Inside inner ---')
        print(y)
    inner()
    print('--- Inside outer ---')
    print(x)
#Run the function chain
outer()
#  Closure Example
# Function returns another function that remembers the value of counter
# A closure is when an inner function remembers the values from its outer function even after the outer function has finished.
def counter_banao():
    counter = 0
    def gino():
        nonlocal counter  # This allows us to modify 'counter' from outer function
        counter += 1
        return counter
    return gino  # We return the function, not call it
# Create a new counter instance
ginti = counter_banao()
# Each call to ginti() will remember the previous count
print("Counter Example:")
print(ginti())  # 1
print(ginti())  # 2
print(ginti())  # 3


#  Scope Example
name = " I'm Global"

def outer_func():
    outer_var = " I'm from Outer"

    def inner_func():
        inner_var = " I'm from Inner"
        print("Accessing everything inside inner_func:")
        print(name)         # Global
        print(outer_var)    # From outer_func
        print(inner_var)    # From inner_func
    inner_func()
outer_func()
#  Function Factory using Closure
# This function creates multiplier functions
#  A factory function is a function that creates and returns another function.
def multiplier(factor):
    def multiply(number):
        return number * factor  # Remembers 'factor' from the parent
    return multiply
double = multiplier(2)
triple = multiplier(3)
print("Double of 5:", double(5) )   # 10
print("Triple of 5:", triple(5))   # 15


