
# Print each letter in a string
for i in "Giraffe Academy":
    print(i)
print

# Print each object in an array
for i in ["Jim","Karen","Kevin"]:
    print(i)
print

friends = ["Tom","Maria","Brandon", "Tyler"]
for i in friends:
    print(i)
print

# Range and index (range starts at 0)
for index in range(10):
    print(index)
print

for index in range(3, 10):
    print(index)
print

for index in range(len(friends)):
    print(index)
print

# Like print(friends[0], friends[1], friends[2], friends[3])
for index in range(len(friends)):
    print(friends[index])
print
print(friends[0], friends[1], friends[2], friends[3])
print

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first Iteration")
print