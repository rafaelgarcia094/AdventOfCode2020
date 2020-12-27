def rotate_right(east, north):
    return north, -east


def rotate_left(east, north):
    return -north, east


current_east_pos = 0
current_north_pos = 0

waypoint_east_pos = 10
waypoint_north_pos = 1

for _ in range(747):
    instruction = input()
    movement = instruction[0]
    value = int(instruction[1:])

    if movement == 'N':
        waypoint_north_pos += value
    if movement == 'S':
        waypoint_north_pos -= value
    if movement == 'E':
        waypoint_east_pos += value
    if movement == 'W':
        waypoint_east_pos -= value
    if movement == 'L':
        for i in range(value // 90):
            waypoint_east_pos, waypoint_north_pos = rotate_left(waypoint_east_pos, waypoint_north_pos)
    if movement == 'R':
        for i in range(value // 90):
            waypoint_east_pos, waypoint_north_pos = rotate_right(waypoint_east_pos, waypoint_north_pos)
    if movement == 'F':
        current_east_pos += waypoint_east_pos * value
        current_north_pos += waypoint_north_pos * value

manhattan_distance = abs(current_east_pos) + abs(current_north_pos)
print(manhattan_distance)
