# two dimensional list (list in a list is a grid, 4 rows 3 columns)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# what is at row zero column zero
print(number_grid[0][0])
print
# what is at row 2 column 1
print(number_grid[2][1])
print

# Parse a two dimensional array with nested loops
for row in number_grid:
    # print(row)
    for col in row:
        print(col)