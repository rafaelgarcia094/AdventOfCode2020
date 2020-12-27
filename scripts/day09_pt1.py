preamble = [int(input()) for _ in range(25)]

for _ in range(975):
    x = int(input())

    valid = False
    for i, a in enumerate(preamble[:-1]):
        for b in preamble[i+1:]:
            if a + b == x:
                valid = True

    if not valid:
        print(x)
        break

    preamble = preamble[1:] + [x]
