tile_colors = {}

for _ in range(400):
    path = input()

    i = 0
    pos_north = 0.0
    pos_east = 0.0

    while i < len(path):
        if path[i] == 'e':
            pos_east += 1.0
            i += 1
        elif path[i] == 'w':
            pos_east -= 1.0
            i += 1
        elif path[i] == 'n' and path[i+1] == 'e':
            pos_north += 0.5
            pos_east += 0.5
            i += 2
        elif path[i] == 's' and path[i+1] == 'e':
            pos_north -= 0.5
            pos_east += 0.5
            i += 2
        elif path[i] == 's' and path[i+1] == 'w':
            pos_north -= 0.5
            pos_east -= 0.5
            i += 2
        else:
            pos_north += 0.5
            pos_east -= 0.5
            i += 2

    pos = (pos_east, pos_north)

    if pos in tile_colors:
        tile_colors[pos] = 'black' if tile_colors.get(pos) == 'white' else 'white'
    else:
        tile_colors[pos] = 'black'

counter = 0

for pos in tile_colors.keys():
    if tile_colors.get(pos) == 'black':
        counter += 1

print(counter)
