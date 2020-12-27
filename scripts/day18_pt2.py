import re


def find_operation(expr, op):
    idx = len(expr) - 1

    while expr[idx] != op and idx > 0:
        if expr[idx] == ')':
            parenthesis_counter = 1

            while parenthesis_counter > 0:
                idx -= 1
                if expr[idx] == ')':
                    parenthesis_counter += 1
                if expr[idx] == '(':
                    parenthesis_counter -= 1
        else:
            idx -= 1

    return idx


def check_encapsulation(expr):
    counter = 1
    idx = 1

    while idx < len(expr)-1 and counter > 0:
        if expr[idx] == '(':
            counter += 1
        if expr[idx] == ')':
            counter -= 1

        idx += 1

    return counter > 0


class Expression:
    def __init__(self, expr):
        if len(expr) == 1:
            self.operation = '*'
            self.left = 1
            self.right = int(expr[0])
            return

        if expr[0] == '(' and check_encapsulation(expr):
            expr = expr[1:-1]

        op = '*'
        idx = find_operation(expr, op)

        if idx == 0:
            op = '+'
            idx = find_operation(expr, op)

        self.operation = op
        self.left = Expression(expr[:idx])
        self.right = Expression(expr[idx + 1:])

    def evaluate(self):
        a = self.left if type(self.left) == int else self.left.evaluate()
        b = self.right if type(self.right) == int else self.right.evaluate()
        return a + b if self.operation == '+' else a * b


result = 0
for _ in range(373):
    expression = input()
    expression = re.findall(r'\d+|[*+()]', expression)
    expr_tree = Expression(expression)
    result += expr_tree.evaluate()

print(result)
