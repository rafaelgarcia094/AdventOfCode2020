preamble = [int(input()) for _ in range(25)]

invalid_number = -1
for _ in range(975):
    x = int(input())

    valid = False
    for i, a in enumerate(preamble[-25:-1]):
        for b in preamble[-24+i:]:
            if a + b == x:
                valid = True

    if not valid:
        invalid_number = x
        break

    preamble.append(x)

start, end = 0, 1
total_sum = preamble[start] + preamble[end]

while total_sum != invalid_number:
    if total_sum < invalid_number:
        end += 1
        total_sum += preamble[end]
    else:
        total_sum -= preamble[start]
        start += 1

min_v = invalid_number
max_v = 0

for i in range(start, end+1):
    min_v = min(min_v, preamble[i])
    max_v = max(max_v, preamble[i])

print(max_v + min_v)
