def str_measure(s):
    r = ''.join([str('LRFB'.find(c)) for c in s])
    return r


ticket = 'FFFFFFFLLL'

for _ in range(757):
    new_ticket = input()
    ticket = max(ticket, new_ticket, key=str_measure)

ticket_id, step = 0, 64

for i in range(7):
    if ticket[i] == 'B':
        ticket_id += step
    step //= 2

ticket_id *= 8
step = 4

for i in range(3):
    if ticket[7+i] == 'R':
        ticket_id += step
    step //= 2

print(ticket_id)
