sequence = list(map(int, input().split(',')))
last_appearance = {}

for i in range(len(sequence)):
    last_appearance[sequence[i]] = i + 1

next_number = 0
for i in range(len(sequence) + 1, 30000000):
    if next_number not in last_appearance:
        last_appearance[next_number] = i
        next_number = 0
    else:
        aux_mem = next_number
        next_number = i - last_appearance[next_number]
        last_appearance[aux_mem] = i

print(next_number)
