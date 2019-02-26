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