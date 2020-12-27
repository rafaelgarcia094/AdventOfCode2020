import re

memory = {}
mask = ''

for _ in range(545):
    line = input()

    if line[:4] == 'mask':
        mask = line[7:]
        continue

    memory_position, value = map(int, re.findall(r'[0-9]+', line))
    binary_string = format(value, f'0{len(mask)}b')

    for i in range(len(mask)):
        if mask[i] != 'X':
            binary_string = binary_string[:i] + mask[i] + binary_string[i+1:]

    memory[memory_position] = int(binary_string, 2)

result = sum(memory.values())
print(result)
