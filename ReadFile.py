# reading an external file

# open the file and close a file
employee_file = open("TextFile.txt", "r") # "r = read only" "w = write" "a = append to file" "r+ = read write"

# print(employee_file.readable()) # checks if file is readable
# print(employee_file.read()) # Actually read the file
print
# print(employee_file.readlines()) # read a line from the file
print
# print(employee_file.readlines()[1]) # read a line from the file


for employee in employee_file.readlines():
    print(employee)

employee_file.close()


# Write and Append
employee_file = open("TextFile.txt", "a") # add text at file end

employee_file.write("Tom - Programmer")
employee_file.write("\nKelly - Cust Service") # adds to new line

employee_file.close()

employee_file = open("TextFile1.txt", "w") # add text at file end

employee_file.write("\nTom - Programmer")
employee_file.write("\nKelly - Cust Service") # adds to new line

employee_file.close()

