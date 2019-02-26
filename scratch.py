from math import *

Name = "John"
Age = "35"
My_Num = -5
print("There once was a man named " + Name)
print("he was " + Age + " years old.  ")
print("He really didn't like the name " + Name + ".  ")
# Order of operation
print(3 * (4 + My_Num))
# Devided
print(10/My_Num)
# "MOD" gives the remainder
print(10 % My_Num)
# turn a number to a string for concatenation
print (str(My_Num) + " is my favorite number.  ")
# Absolute Value
print(My_Num)
# 3 to the power of 2
print(pow(3, 2))
# largest number, min gives lowest
print(max(3, 2))
print(min(3, 2))
# floor, ceil take the lowest or highest, round off, square root
print(floor(3.7))
print(ceil(3.7))
print(round(3.7))
print(sqrt(36))

# Get User Input, for string, use raw_input in 2.x and input in 3.x
your_name = raw_input("Enter your name: ")
your_age = raw_input("Enter your age: ")
print("Hello " + your_name + "!  You are " + your_age)

Num1 = input("Enter a number: ")
Num2 = input("Enter another number: ")
Result1 = int(Num1) + int(Num2)
Result2 = float(Num1) + float(Num2)

print(str(Result1) + " " + str(Result2))

friend = ["Tom", "Maria", "Brandon", "Tyler"]
