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

neighbors = [(-1, 0), (1, 0), (0.5, 0.5), (0.5, -0.5), (-0.5, 0.5), (-0.5, -0.5)]

for i in range(100):
    min_east = min(map(lambda x: x[0], tile_colors.keys())) - 1.0
    max_east = max(map(lambda x: x[0], tile_colors.keys())) + 1.0
    min_north = min(map(lambda x: x[1], tile_colors.keys())) - 0.5
    max_north = max(map(lambda x: x[1], tile_colors.keys())) + 0.5

    a = min_east
    while a <= max_east:
        b = min_north
        while b <= max_north:
            if not((a == int(a)) ^ (b == int(b))) and (a, b) not in tile_colors:
                tile_colors[(a, b)] = 'white'
            b += 0.5
        a += 0.5

    new_tile = {}

    for pos in tile_colors.keys():
        counter = 0

        for step in neighbors:
            neighbor_pos = (pos[0] + step[0], pos[1] + step[1])
            if neighbor_pos in tile_colors and tile_colors.get(neighbor_pos) == 'black':
                counter += 1

        if tile_colors.get(pos) == 'black':
            new_tile[pos] = 'white' if counter == 0 or counter > 2 else 'black'
        else:
            new_tile[pos] = 'black' if counter == 2 else 'white'

    tile_colors = new_tile

counter = 0

for pos in tile_colors.keys():
    if tile_colors.get(pos) == 'black':
        counter += 1

print(counter)
