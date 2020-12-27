total_answers = 0
new_group = True

for _ in range(2132):
    if new_group:
        questions = set(input())
        new_group = False
        continue

    line = input()

    if line == '':
        total_answers += len(questions)
        new_group = True
        continue

    questions = questions.intersection(set(line))

print(total_answers)
