import re

rule_book = {}


def evaluate_rule(rule_n):
    if rule_book[rule_n][0][0] == '\"':
        return rule_book[rule_n][0][1:-1]

    evaluated_rule = []

    for rule in rule_book[rule_n]:
        if '0' <= rule[0] <= '9':
            if int(rule) != 11:
                evaluated_rule.append('(')

            evaluated_rule.append(evaluate_rule(int(rule)))

            if int(rule) != 11:
                evaluated_rule.append(')')

            if rule_n == 8:
                evaluated_rule.append('+')
            if rule_n == 11 and rule == '42':
                evaluated_rule.append('11')

        if rule[0] == '|':
            evaluated_rule.append('|')

    return ''.join(evaluated_rule)


while (rule_line := input()) != '':
    rule_number, rules = rule_line.split(': ')
    rule_book[int(rule_number)] = rules.split(' ')

final_rule = evaluate_rule(0)
recursive_rule = evaluate_rule(11)
prefix_rule, suffix_rule = final_rule.split('11')
prefix_recursive, suffix_recursive = recursive_rule.split('11')

matched_messages = 0
while True:
    try:
        message = input()
    except EOFError:
        break

    matched = False
    for i in range(5):
        final_rule = prefix_rule + prefix_recursive * i + suffix_recursive * i + suffix_rule

        if re.fullmatch(rf'{final_rule}', message):
            matched = True
            break

    if matched:
        matched_messages += 1

print(matched_messages)
