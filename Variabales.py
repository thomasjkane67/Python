friend = ["Tom", "Maria", "Brandon", "Tyler"]
numbers = [2, 10, 15, 25, 75]
print(friend + numbers)
friend.extend(numbers)
print(friend)
friend.append("Creed")
print(friend)
friend.insert(1, "Kelly")
print(friend)
friend.remove("Brandon")
print(friend)
# Pop last element off the array
friend.pop()
# Where is "Maria" in the list
print(friend.index("Maria"))
# count how often an element occurs
print(friend.count("Tyler"))
friend.sort()
print(friend)
friend.reverse()
print(friend)
my_friends = friend.copy()
print(my_friends)
