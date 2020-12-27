def calc_id(ticket):
    ticket_id, step = 0, 64

    for i in range(7):
        if ticket[i] == 'B':
            ticket_id += step
        step //= 2

    ticket_id *= 8
    step = 4

    for i in range(3):
        if ticket[7 + i] == 'R':
            ticket_id += step
        step //= 2

    return ticket_id


tickets = sorted([calc_id(input()) for _ in range(757)])

for i in range(len(tickets)-1):
    if tickets[i] + 2 == tickets[i+1]:
        print(tickets[i] + 1)
