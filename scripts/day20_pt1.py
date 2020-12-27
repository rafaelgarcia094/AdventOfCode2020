from collections import Counter
from math import prod

tiles = {}


def add_border(tile_border, tile_id):
    if tile_border in tiles:
        tiles[tile_border].add(tile_id)
    elif tile_border[::-1] in tiles:
        tiles[tile_border[::-1]].add(tile_id)
    else:
        tiles[tile_border] = set()
        tiles[tile_border].add(tile_id)


def save_tile(tile_grid, tile_id):
    add_border(tile_grid[0], tile_id)
    add_border(tile_grid[-1], tile_id)
    add_border(''.join([t[0] for t in tile_grid]), tile_id)
    add_border(''.join([t[-1] for t in tile_grid]), tile_id)


end_of_file = False
current_id = -1
current_tile = []

while not end_of_file:
    try:
        line = input()

        if line == '':
            save_tile(current_tile, current_id)

        elif line.startswith('Tile'):
            current_id = int(line[5:-1])
            current_tile = []

        else:
            current_tile.append(line)

    except EOFError:
        save_tile(current_tile, current_id)
        end_of_file = True

border_list = []

for tile in tiles.keys():
    if len(tiles[tile]) == 1:
        border_list.append(list(tiles[tile])[0])

corners = [x for x, c in Counter(border_list).items() if c > 1]

print(prod(corners))
