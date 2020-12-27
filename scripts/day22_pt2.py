n_cards = 25

_ = input()
deck1 = [tuple(int(input()) for _ in range(n_cards))]
_ = input()
_ = input()
deck2 = [tuple(int(input()) for _ in range(n_cards))]

past_configs = [set()]

while len(deck1) > 1 or (deck1[0] and deck2[0]):
    d1 = deck1[-1]
    d2 = deck2[-1]

    if d1 + (-1,) in past_configs[-1] or d2 + (-2,) in past_configs[-1]:
        if len(deck1) > 1:
            del deck1[-1]
            del deck2[-1]
            del past_configs[-1]

            deck1[-1] = deck1[-1][1:] + (deck1[-1][0], deck2[-1][0])
            deck2[-1] = deck2[-1][1:]
        else:
            deck2[-1] = tuple()

        continue

    past_configs[-1].add(d1 + (-1,))
    past_configs[-1].add(d2 + (-2,))

    if d1[0] >= len(d1) or d2[0] >= len(d2):
        if d1[0] > d2[0]:
            deck1[-1] = deck1[-1][1:] + (deck1[-1][0], deck2[-1][0])
            deck2[-1] = deck2[-1][1:]
        else:
            deck2[-1] = deck2[-1][1:] + (deck2[-1][0], deck1[-1][0])
            deck1[-1] = deck1[-1][1:]

        if len(deck1[-1]) == 0 and len(deck1) > 1:
            del deck1[-1]
            del deck2[-1]
            del past_configs[-1]

            deck2[-1] = deck2[-1][1:] + (deck2[-1][0], deck1[-1][0])
            deck1[-1] = deck1[-1][1:]

        elif len(deck2[-1]) == 0 and len(deck2) > 1:
            del deck1[-1]
            del deck2[-1]
            del past_configs[-1]

            deck1[-1] = deck1[-1][1:] + (deck1[-1][0], deck2[-1][0])
            deck2[-1] = deck2[-1][1:]

        continue

    new_d1 = d1[1:d1[0] + 1]
    new_d2 = d2[1:d2[0] + 1]

    deck1.append(new_d1)
    deck2.append(new_d2)
    past_configs.append(set())

winner = deck1[0] if deck1[0] else deck2[0]

score = 0

for i, v in enumerate(winner[::-1]):
    score += v * (i + 1)

print(score)

# def game(d1, d2):
#     if d1 + (-1,) in past_configs[-1] or d2 + (-2,) in past_configs[-1]:
#         return 1, d1
#
#     if len(d1) == 0:
#         return 2, d2
#
#     if len(d2) == 0:
#         return 1, d1
#
#     past_configs[-1].add(d1 + (-1,))
#     past_configs[-1].add(d2 + (-2,))
#
#     if d1[0] >= len(d1) or d2[0] >= len(d2):
#         if d1[0] > d2[0]:
#             return game(d1[1:] + (d1[0],) + (d2[0],), d2[1:])
#         else:
#             return game(d1[1:], d2[1:] + (d2[0],) + (d1[0],))
#
#     new_d1 = d1[1:d1[0] + 1]
#     new_d2 = d2[1:d2[0] + 1]
#
#     past_configs.append(set())
#     round_winner, _ = game(new_d1, new_d2)
#     del past_configs[-1]
#
#     if round_winner == 1:
#         return game(d1[1:] + (d1[0],) + (d2[0],), d2[1:])
#     else:
#         return game(d1[1:], d2[1:] + (d2[0],) + (d1[0],))
