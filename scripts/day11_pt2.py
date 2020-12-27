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

            for step_i, step_j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                x = i + step_i
                y = j + step_j
                occupied_cell = False

                while not occupied_cell and 0 <= x < len(grid) and 0 <= y < len(grid[i]):
                    if grid[x][y] == '#':
                        occupied_cell = True
                    if grid[x][y] == 'L':
                        break

                    x += step_i
                    y += step_j

                if occupied_cell:
                    occupied_neighbors += 1

            if grid[i][j] == 'L' and occupied_neighbors == 0:
                next_grid[i][j] = '#'
                stable = False
            elif grid[i][j] == '#' and occupied_neighbors >= 5:
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
