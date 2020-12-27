adapters = sorted([int(input()) for _ in range(104)])

diff_1 = 0
diff_3 = 1
curr_voltage = 0

for next_voltage in adapters:
    diff = next_voltage - curr_voltage

    if diff == 1:
        diff_1 += 1
    elif diff == 3:
        diff_3 += 1
    else:
        raise Exception(f'{curr_voltage}, {next_voltage}')

    curr_voltage = next_voltage

print(diff_1 * diff_3)