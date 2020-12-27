n_cards = 25

_ = input()
deck1 = [int(input()) for _ in range(n_cards)]
_ = input()
_ = input()
deck2 = [int(input()) for _ in range(n_cards)]

while deck1 and deck2:
    if deck1[0] > deck2[0]:
        deck1 += [deck1[0], deck2[0]]
    else:
        deck2 += [deck2[0], deck1[0]]

    del deck1[0]
    del deck2[0]

winner = deck1 if deck1 else deck2

score = 0
for i, v in enumerate(winner[::-1]):
    score += v * (i + 1)
print(score)
