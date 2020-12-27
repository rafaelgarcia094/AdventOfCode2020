from collections import Counter
from math import sqrt

tiles = {}
id_to_grid = {}


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

    id_to_grid[tile_id] = [list(tile_row) for tile_row in tile_grid]


def rotate_grid(tile_grid):
    size = len(tile_grid)
    new_grid = [[tile_grid[size-1-c][r] for c in range(size)] for r in range(size)]
    return new_grid


def flip_grid_vertical(tile_grid):
    size = len(tile_grid)
    new_grid = [[tile_grid[size-1-r][c] for c in range(size)] for r in range(size)]
    return new_grid


def flip_grid_horizontal(tile_grid):
    size = len(tile_grid)
    new_grid = [[tile_grid[r][size-1-c] for c in range(size)] for r in range(size)]
    return new_grid


def match_left_right(tile1, tile2):
    size = len(tile1)

    for r in range(size):
        if tile1[r][size-1] != tile2[r][0]:
            return False

    return True


def match_top_bottom(tile1, tile2):
    size = len(tile1)

    for c in range(size):
        if tile1[size-1][c] != tile2[0][c]:
            return False

    return True


def all_transformations(tile1):
    size = len(tile1)
    new_grid = [[tile1[r][c] for c in range(size)] for r in range(size)]
    transformations = []

    for _ in range(4):
        transformations.append(new_grid)
        transformations.append(flip_grid_vertical(new_grid))
        transformations.append(flip_grid_horizontal(new_grid))
        new_grid = rotate_grid(new_grid)

    return transformations


def is_monster(image, monster, r, c):
    for ri in range(len(monster)):
        for ci in range(len(monster[0])):
            if monster[ri][ci] == '#' and image[r+ri][c+ci] != '#':
                return False

    return True


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

neighbour_id = {v: set() for v in id_to_grid.keys()}
for s in tiles.values():
    if len(s) == 2:
        a, b = tuple(s)
        neighbour_id[a].add(b)
        neighbour_id[b].add(a)

border_list = []

for tile in tiles.keys():
    if len(tiles[tile]) == 1:
        border_list.append(list(tiles[tile])[0])

corners = [x for x, c in Counter(border_list).items() if c > 1]

image_size = int(sqrt(len(id_to_grid.keys())))

image_ids = [[-1 for _ in range(image_size)] for _ in range(image_size)]
image_ids[0][0] = corners[0]

for i in range(image_size-1):
    for j in range(image_size):
        c = image_ids[i][j]
        neighbors = tuple(neighbour_id[c])

        if len(neighbors) == 1:
            image_ids[i+1][j] = neighbors[0]
            neighbour_id[neighbors[0]].remove(c)
            continue

        a, b = neighbors

        if j == 0 and i == 0:
            image_ids[1][0] = a
            image_ids[0][1] = b

        elif j == 0:
            image_ids[i][j+1] = a if a in neighbour_id[image_ids[i-1][j+1]] else b
            image_ids[i+1][j] = b if a in neighbour_id[image_ids[i-1][j+1]] else a

        else:
            image_ids[i+1][j] = a if a in neighbour_id[image_ids[i+1][j-1]] else b
            image_ids[i][j+1] = b if a in neighbour_id[image_ids[i+1][j-1]] else a

        neighbour_id[a].remove(c)
        neighbour_id[b].remove(c)

trans_tile00 = all_transformations(id_to_grid[image_ids[0][0]])
trans_tile01 = all_transformations(id_to_grid[image_ids[0][1]])
trans_tile10 = all_transformations(id_to_grid[image_ids[1][0]])

trans_id00, trans_id01, trans_id10 = -1, -1, -1
for i in range(len(trans_tile00)):
    for j in range(len(trans_tile01)):
        for k in range(len(trans_tile10)):
            if match_left_right(trans_tile00[i], trans_tile01[j]) and \
                    match_top_bottom(trans_tile00[i], trans_tile10[k]):
                trans_id00 = i
                trans_id01 = j
                trans_id10 = k

id_to_grid[image_ids[0][0]] = trans_tile00[trans_id00]
id_to_grid[image_ids[0][1]] = trans_tile01[trans_id01]
id_to_grid[image_ids[1][0]] = trans_tile10[trans_id01]

for i in range(2, image_size):
    next_tile_trans = all_transformations(id_to_grid[image_ids[0][i]])

    for trans in next_tile_trans:
        if match_left_right(id_to_grid[image_ids[0][i-1]], trans):
            id_to_grid[image_ids[0][i]] = trans

for i in range(1, image_size):
    for j in range(image_size):
        next_tile_trans = all_transformations(id_to_grid[image_ids[i][j]])

        for trans in next_tile_trans:
            if match_top_bottom(id_to_grid[image_ids[i-1][j]], trans):
                id_to_grid[image_ids[i][j]] = trans

border_size = len(list(tiles.keys())[0]) - 2
full_image_size = image_size*border_size

full_image = [['.' for _ in range(full_image_size)] for _ in range(full_image_size)]

for i in range(image_size):
    for j in range(image_size):
        g = id_to_grid[image_ids[i][j]]

        for x in range(1, len(g)-1):
            for y in range(1, len(g[0])-1):
                full_image[i*border_size + x - 1][j*border_size + y - 1] = g[x][y]

all_images = all_transformations(full_image)

sea_monster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']

set_images = set()
unique_images = []
for img in all_images:
    str_image = ''.join([''.join(row) for row in img])

    if str_image not in set_images:
        set_images.add(str_image)
        unique_images.append(img)

n_monsters = 0

for img in unique_images:
    for i in range(len(img) - len(sea_monster) + 1):
        for j in range(len(img[0]) - len(sea_monster[0]) + 1):
            if is_monster(img, sea_monster, i, j):
                n_monsters += 1

    if n_monsters > 0:
        break

n_hashes = [c for x, c in Counter(list(set_images)[0]).items() if x == '#'][0]
roughness = n_hashes - (15*n_monsters)

print(roughness)
