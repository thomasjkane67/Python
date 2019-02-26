# Python

| Description | Example | Comments |
| ------------- | ------------- | ------------- |
| Variable | friend = "Tom" | "" is a string, froce numbers to string with str() |
|| from math import * ||
|| Name = "John"||
|| Age = "35"||
|| My_Num = -5||
|| print("There once was a man named " + Name)||
|| print("he was " + Age + " years old.  ")||
|| print("He really didn't like the name " + Name + ".  ")||
|# Order of operation|||
||print(3 * (4 + My_Num))||
|# Devided|||
||print(10/My_Num)||
|# "MOD" gives the remainder|||
||print(10 % My_Num)||
|# turn a number to a string for concatenation|||
||print (str(My_Num) + " is my favorite number.  ")||
|# Absolute Value|||
||print(My_Num)||
|# 3 to the power of 2|||
||print(pow(3, 2))||
|# largest number, min gives lowest|||
||print(max(3, 2))||
||print(min(3, 2))||
|# floor, ceil take the lowest or highest, round off, square root|||
||print(floor(3.7))||
||print(ceil(3.7))||
||print(round(3.7))||
||print(sqrt(36))||
| Variable | friend = ["Tom", "Maria", "Brandon", "Tyler"] | This is a list |
|| print(friend[2]) | Brandon | 
|| print(friend[1:])| "Maria", "Brandon", "Tyler" |
|| print(friend[1:3])| "Maria", "Brandon" |
|| print(friend[-1])| Tyler |
|| frined[1] = "Frank" | Change "Maria" to Frank" |
|| numbers = [2, 10, 15, 25, 75]||
|| print(friend + numbers)||
| Variable.extend | friend.extend(numbers) | Append lists together |
||print(friend)||
| Variable.append | friend.append("Creed")|  |
||print(friend)||
| Variable.inset | friend.insert(1, "Kelly")|  |
||print(friend)||
||friend.remove("Brandon")||
||print(friend)||
|# Pop last element off the array|||
||friend.pop()||
|# Where is "Maria" in the list|||
||print(friend.index("Maria"))||
|# count how often an element occurs|||
||print(friend.count("Tyler"))||
||friend.sort()||
||print(friend)||
||friend.reverse()||
||print(friend)||
||my_friends = friend.copy()||
||print(my_friends)||
|Tuple|my_tuple = (4, 5)|Lists can be modified, tuples can not|
||print(my_tuple[0])||
||print(my_tuple[1])||
||tuple_list[(4, 5),(6, 7),(20, 25)] | Tuples can be inside a list
| Functions | Group of code to perform a task | Call the function|
||def my_function():|Won't exacute untill called|
||... print("Hello there") | what to do|
||my_function()|| Call to the function||
||# Functions don't run until called, code nust be indented


# Function
```
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

my_function3("Tom", 52)|
```


# Comparison
```
def max_num(num1, num2, num3):
    if num1 >= num3 and num1 >= num3:
        return str(num1) + " is greater then " + str(num2) + " and " + str(num3)
    elif num2 >= num1 and num2 >= num3:
        return str(num2) + " is greater then " + str(num1) + " and " + str(num3)
    elif num3 >= num1 and num3 >= num2:
        return str(num3) + " is greater then " + str(num1) + " and " + str(num2)

# result = max_num(10, 5, 15)
# == equals != not equal
# >= equal or greater
# < less than
print(max_num(10, 5, 15))

def max_str(str1, str2, str3):
    if str1 == "dog":
        return str1
    elif str1 == "cat":
        return str1
    elif str1 == "bird":
        return str1

print(max_str("bird", "cat", "dog"))

def my_calclator():
    num1 = float(input("Enter a number: "))
    op = raw_input("Enter a operator, + - / *: ")
    num2 = float(input("Enter a number: "))
    if op == "+":
        return (num1 + num2)
    elif op == "-":
        return (num1 - num2)
    elif op == "*":
        return (num1 * num2)
    elif op == "/":
        return (num1 / num2)
    else:
        print("Invalid operator? ")

print(my_calclator())
```
# Dictionaries
```
# Dictionaries are stored in key and value pairs
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "Decemeber",
}
print(monthConversions["Nov"])
print(monthConversions["Mar"])
# With GET you can specify a default value
print(monthConversions.get("Dec"))
print(monthConversions.get("Wrong", "Not a valid key "))

# Keys can be strings or numbers
monthConversionsN = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "Decemeber",
}
print(monthConversionsN[9])
```
