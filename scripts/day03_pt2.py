grid = [input() for _ in range(323)]

width = len(grid[0])
height = len(grid)

multiplication = 1
down = [1, 1, 1, 1, 2]
right = [1, 3, 5, 7, 1]

for d, r in zip(down, right):
    trees = 0

    i, j = 0, 0
    while (i := i + d) < height:
        j = (j + r) % width

        if grid[i][j] == '#':
            trees += 1

    multiplication *= trees

print(multiplication)
