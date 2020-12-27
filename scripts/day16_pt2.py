from math import prod

range_list = []
attribute_list = {}

while (line := input()) != '':
    attribute_name, value_text = line.split(': ')
    first_range, second_range = value_text.split(' or ')
    a, b = map(int, first_range.split('-'))
    c, d = map(int, second_range.split('-'))

    range_list.append((a, b))
    range_list.append((c, d))

    attribute_list[attribute_name] = (a, b, c, d)

range_list.sort()

_ = input()

my_ticket = list(map(int, input().split(',')))

_ = input()
_ = input()

valid_tickets = [my_ticket]

while True:
    try:
        line = input()
    except EOFError:
        break

    ticket = list(map(int, line.split(',')))
    sorted_ticket = sorted(ticket)
    is_valid = True

    i, j = 0, 0
    while is_valid and i < len(sorted_ticket) and j < len(range_list):
        if range_list[j][0] <= sorted_ticket[i] <= range_list[j][1]:
            i += 1
        elif sorted_ticket[i] < range_list[j][0]:
            is_valid = False
            i += 1
        else:
            j += 1

    if is_valid and i >= len(sorted_ticket):
        valid_tickets.append(ticket)

idx_per_attribute = {name: set([i for i in range(len(my_ticket))]) for name in attribute_list.keys()}

for ticket in valid_tickets:
    for i in range(len(ticket)):
        value = ticket[i]

        for attr_name in attribute_list.keys():
            a, b, c, d = attribute_list[attr_name]

            if (value < a or value > b) and (value < c or value > d) and i in idx_per_attribute[attr_name]:
                idx_per_attribute[attr_name].remove(i)

attr_to_ticket = {}

for _ in range(len(idx_per_attribute.keys())):
    key = ''
    ticket = -1

    for k in idx_per_attribute.keys():
        if len(idx_per_attribute[k]) == 1:
            key = k
            ticket = list(idx_per_attribute[k])[0]
            break

    if key.startswith('departure'):
        attr_to_ticket[key] = ticket

    for k in idx_per_attribute.keys():
        if ticket in idx_per_attribute[k]:
            idx_per_attribute[k].remove(ticket)

result = prod([my_ticket[idx] for idx in attr_to_ticket.values()])

print(result)
