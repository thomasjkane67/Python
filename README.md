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
||    print("Hello there") | what to do|
||my_function()|| Call to the function||
||||
||||
