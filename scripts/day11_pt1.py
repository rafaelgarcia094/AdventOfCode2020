grid = [list(input()) for _ in range(97)]

stable = False
while not stable:
    next_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    stable = True

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                continue

            occupied_neighbors = 0

            for x in range(max(0, i-1), min(len(grid), i+2)):
                for y in range(max(0, j-1), min(len(grid[i]), j+2)):
                    if (i != x or j != y) and grid[x][y] == '#':
                        occupied_neighbors += 1

            if grid[i][j] == 'L' and occupied_neighbors == 0:
                next_grid[i][j] = '#'
                stable = False
            elif grid[i][j] == '#' and occupied_neighbors >= 4:
                next_grid[i][j] = 'L'
                stable = False
            else:
                next_grid[i][j] = grid[i][j]

    grid = next_grid

total_occupied = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            total_occupied += 1

print(total_occupied)
