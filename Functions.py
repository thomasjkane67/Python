# Functions don't run until called, code nust be indented
def my_function():
    print("Hello there " )

my_function()

# Parameters can be passed to a function
def my_function1(name):
    print("Hello there " + name )

my_function1("Tom")

# Multiple parameters can be passed to the function
def my_function2(name, age):
    print("Hello there " + name + " you are " + age )

my_function2("Tom", "52")

# Multiple parameters can be passed numbers can be used with strings
def my_function3(name, age):
    print("Hello there " + name + " you are " + str(age) )

my_function3("Tom", 52)

# Use return statement with functions
def cube_function(num):
    return num*num*num

print(cube_function(4))

# Store return in a variable
def cube_function1(num):
    return num*num*num

result = cube_function1(4)
print(result)