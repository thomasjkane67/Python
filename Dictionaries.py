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