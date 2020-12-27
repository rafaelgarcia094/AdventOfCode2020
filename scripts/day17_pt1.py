grid_size = 8
cycles = 6

grid = [[[c for c in input()] for _ in range(grid_size)]]

for i in range(grid_size):
    grid[0][i] = ['.' for _ in range(cycles)] + grid[0][i] + ['.' for _ in range(cycles)]

for _ in range(cycles):
    grid[0] = [['.' for _ in range(grid_size + cycles * 2)]] + grid[0] + [['.' for _ in range(grid_size + cycles * 2)]]

for _ in range(cycles):
    grid = [[['.' for _ in range(grid_size + cycles * 2)] for _ in range(grid_size + cycles * 2)]] + grid + \
           [[['.' for _ in range(grid_size + cycles * 2)] for _ in range(grid_size + cycles * 2)]]

for _ in range(cycles):
    new_grid = [[['.' for _ in range(len(grid[0][0]))] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for z in range(len(grid)):
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                active_neighbours = 0

                for i in range(max(0, z-1), min(z+2, len(grid))):
                    for j in range(max(0, y-1), min(y+2, len(grid[z]))):
                        for k in range(max(x-1, 0), min(x+2, len(grid[z][y]))):
                            if grid[i][j][k] == '#' and (i != z or j != y or k != x):
                                active_neighbours += 1

                if grid[z][y][x] == '#':
                    new_grid[z][y][x] = '#' if 2 <= active_neighbours <= 3 else '.'
                else:
                    new_grid[z][y][x] = '#' if active_neighbours == 3 else '.'

    grid = new_grid

counter = 0
for z in range(len(grid)):
    for y in range(len(grid[z])):
        for x in range(len(grid[z][y])):
            if grid[z][y][x] == '#':
                counter += 1

print(counter)
