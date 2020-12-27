code = [input() for _ in range(610)]

instr_idx = 0
acc_value = 0
executed_ops = set()

while instr_idx not in executed_ops:
    executed_ops.add(instr_idx)
    operation = code[instr_idx]

    if operation[:3] == 'acc':
        acc_value += int(operation[4:])
        instr_idx += 1
    if operation[:3] == 'jmp':
        instr_idx += int(operation[4:])
    if operation[:3] == 'nop':
        instr_idx += 1

print(acc_value)
