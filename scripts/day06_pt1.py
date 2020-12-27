total_answers = 0
questions = set()

for _ in range(2132):
    line = input()

    if line == '':
        questions = set()
        continue

    for c in line:
        if c not in questions:
            questions.add(c)
            total_answers += 1

print(total_answers)
