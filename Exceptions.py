
# try a code and skip if failed
try:
    number = int(input("Enter a number: "))
    print
    print(number)
except: # to broad of an exception
    print("You didn't enter a number!")
print

try:
    # value = 10 /0
    number = int(input("Enter a number: "))
    print
    print(number)
except ZeroDivisionError: # Handles 10 divided by 0
    print("Divide by zero!")
except ValueError: # handles input error
    print("invalid input!")
print

try:
    value = 10 /0
    number = int(input("Enter a number: "))
    print
    print(number)
except ZeroDivisionError as err: # Store error to a variable
    print(err)
except ValueError: # handles input error
    print("invalid input!")


