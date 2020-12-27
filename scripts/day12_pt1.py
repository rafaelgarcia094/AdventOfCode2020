delta_vector = [(1, 0), (0, -1), (-1, 0), (0, 1)]

current_east_pos = 0
current_north_pos = 0
current_delta = 0

for _ in range(747):
    instruction = input()
    movement = instruction[0]
    value = int(instruction[1:])

    if movement == 'N':
        current_north_pos += value
    if movement == 'S':
        current_north_pos -= value
    if movement == 'E':
        current_east_pos += value
    if movement == 'W':
        current_east_pos -= value
    if movement == 'L':
        current_delta = (current_delta - (value // 90)) % 4
    if movement == 'R':
        current_delta = (current_delta + (value // 90)) % 4
    if movement == 'F':
        current_east_pos += delta_vector[current_delta][0] * value
        current_north_pos += delta_vector[current_delta][1] * value

manhattan_distance = abs(current_east_pos) + abs(current_north_pos)
print(manhattan_distance)
