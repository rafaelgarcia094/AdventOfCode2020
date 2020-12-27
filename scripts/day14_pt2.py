import re


class Memory:
    def __init__(self):
        self.node_0 = None
        self.node_1 = None
        self.value = 0

    def add_binary_string(self, bin_string, mem_value):
        if len(bin_string) == 0:
            self.value = mem_value
            return

        if bin_string[0] != '1':
            if not self.node_0:
                self.node_0 = Memory()
            self.node_0.add_binary_string(bin_string[1:], mem_value)

        if bin_string[0] != '0':
            if not self.node_1:
                self.node_1 = Memory()
            self.node_1.add_binary_string(bin_string[1:], mem_value)

    def get_memory_sum(self):
        summation = self.value

        if self.node_0:
            summation += self.node_0.get_memory_sum()
        if self.node_1:
            summation += self.node_1.get_memory_sum()

        return summation


memory = Memory()
mask = ''

for _ in range(545):
    line = input()

    if line[:4] == 'mask':
        mask = line[7:]
        continue

    memory_position, value = map(int, re.findall(r'[0-9]+', line))
    binary_string = format(memory_position, f'0{len(mask)}b')

    for i in range(len(mask)):
        if mask[i] == '1':
            binary_string = binary_string[:i] + '1' + binary_string[i + 1:]
        if mask[i] == 'X':
            binary_string = binary_string[:i] + 'X' + binary_string[i + 1:]

    memory.add_binary_string(binary_string, value)

result = memory.get_memory_sum()
print(result)
