numbers_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(numbers_grid)
print("")
print(numbers_grid[1])
print("")

print(numbers_grid[0][0])
print(numbers_grid[0][1])
print(numbers_grid[1][0])

print("")

#Important
for row in numbers_grid:
    for col in row:
        print(col)