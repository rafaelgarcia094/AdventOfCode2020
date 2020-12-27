range_list = []

while (line := input()) != '':
    _, value_text = line.split(': ')
    first_range, second_range = value_text.split(' or ')
    a, b = map(int, first_range.split('-'))
    c, d = map(int, second_range.split('-'))

    range_list.append((a, b))
    range_list.append((c, d))

range_list.sort()

_ = input()

my_ticket = list(map(int, input().split(',')))

_ = input()
_ = input()

error_rate = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    ticket = sorted(list(map(int, line.split(','))))

    i, j = 0, 0
    while i < len(ticket) and j < len(range_list):
        if range_list[j][0] <= ticket[i] <= range_list[j][1]:
            i += 1
        elif ticket[i] < range_list[j][0]:
            error_rate += ticket[i]
            i += 1
        else:
            j += 1

    for v in ticket[i:]:
        error_rate += v

print(error_rate)
