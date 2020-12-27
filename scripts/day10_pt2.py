adapters = [[0, 1]] + sorted([[int(input()), 0] for _ in range(104)])

for i in range(len(adapters)-1):
    voltage, amount = adapters[i]

    for j in range(i+1, min(i+4, len(adapters))):
        next_voltage = adapters[j][0]

        if next_voltage - voltage <= 3:
            adapters[j][1] += amount

print(adapters[-1][1])
