s = set()

for _ in range(200):
    n = int(input())

    if n in s:
        r = n * (2020 - n)
        print(r)
    else:
        s.add(2020 - n)
