import re

result = 0
for _ in range(373):
    expression = input()
    expression = re.findall(r'\d+|[*+()]', expression)

    operation_stack = []
    current_value = 0
    current_operation = '+'

    for x in expression:
        if x == '(':
            operation_stack.append((current_value, current_operation))
            current_value = 0
            current_operation = '+'
        elif x == ')':
            stacked_value, stacked_operation = operation_stack[-1]

            if stacked_operation == '+':
                current_value += stacked_value
            else:
                current_value *= stacked_value

            operation_stack = operation_stack[:-1]
        elif x == '+':
            current_operation = '+'
        elif x == '*':
            current_operation = '*'
        else:
            if current_operation == '+':
                current_value += int(x)
            else:
                current_value *= int(x)

    result += current_value

print(result)
