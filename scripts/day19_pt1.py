import re

rule_book = {}


def evaluate_rule(rule_n):
    if rule_book[rule_n][0][0] == '\"':
        return rule_book[rule_n][0][1:-1]

    evaluated_rule = []

    for rule in rule_book[rule_n]:
        if '0' <= rule[0] <= '9':
            evaluated_rule.append('(')
            evaluated_rule.append(evaluate_rule(int(rule)))
            evaluated_rule.append(')')
        if rule[0] == '|':
            evaluated_rule.append('|')

    return ''.join(evaluated_rule)


while (rule_line := input()) != '':
    rule_number, rules = rule_line.split(': ')
    rule_book[int(rule_number)] = rules.split(' ')

final_rule = evaluate_rule(0)

matched_messages = 0
while True:
    try:
        message = input()
    except EOFError:
        break

    if re.fullmatch(rf'{final_rule}', message):
        matched_messages += 1

print(matched_messages)
