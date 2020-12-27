grid = [input() for _ in range(323)]

width = len(grid[0])
height = len(grid)

trees = 0

i, j = 0, 0
while (i := i + 1) < height:
    j = (j + 3) % width

    if grid[i][j] == '#':
        trees += 1

print(trees)
