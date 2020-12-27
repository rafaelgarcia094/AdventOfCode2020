"""
    Followed algorithm on https://www.youtube.com/watch?v=zIFehsBHB8o&feature=youtu.be

    17,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,13

    x === 0 (mod 17)
    x === (41 - 7) (mod 41)
"""
from math import prod

_ = input()
buses = list(map(lambda c: 1 if c == 'x' else int(c), input().split(',')))
buses = list(filter(lambda elem: elem[0] != 1, [(v, i) for i, v in enumerate(buses)]))

for i in range(len(buses)):
    v, p = buses[i]

    while v < p:
        p -= v

    buses[i] = (v, p)


buses[1:] = [(n, n - b) for n, b in buses[1:]]

n_buses = list(map(lambda y: y[0], buses))
b_buses = list(map(lambda y: y[1], buses))

N = prod(n_buses)
N_buses = list(map(lambda y: N // y, n_buses))

x_buses = []
for a, b in zip(N_buses, n_buses):
    x = 1

    while (a * x) % b != 1:
        x += 1

    x_buses.append(x)

result = 0

for i in range(len(buses)):
    result += b_buses[i] * N_buses[i] * x_buses[i]

result = result % N

print(result)

# Naive Solution:
# pos, bus_id = max([(v, i) for i, v in enumerate(buses)])
#
# k = 0
# valid = False
# current_time = 0
#
# while not valid:
#     valid = True
#     k += 1
#
#     current_time = k*bus_id - pos
#     for i in range(len(buses)):
#         if (current_time + i) % buses[i] != 0:
#             valid = False
#             break
#
#     print(current_time)
#
# print(current_time)
