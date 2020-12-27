code = [input() for _ in range(610)]

for i in range(len(code)-1):
    if code[i][:3] == 'jmp':
        code[i] = 'nop' + code[i][3:]
    elif code[i][:3] == 'nop':
        code[i] = 'jmp' + code[i][3:]

    instr_idx = 0
    acc_value = 0
    executed_ops = set()

    while instr_idx not in executed_ops and instr_idx < len(code):
        executed_ops.add(instr_idx)
        operation = code[instr_idx]

        if operation[:3] == 'acc':
            acc_value += int(operation[4:])
            instr_idx += 1
        if operation[:3] == 'jmp':
            instr_idx += int(operation[4:])
        if operation[:3] == 'nop':
            instr_idx += 1

    if instr_idx >= len(code):
        print(acc_value)

    if code[i][:3] == 'jmp':
        code[i] = 'nop' + code[i][3:]
    elif code[i][:3] == 'nop':
        code[i] = 'jmp' + code[i][3:]