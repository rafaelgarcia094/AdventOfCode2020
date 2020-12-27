v = [int(input()) for _ in range(200)]

for i in range(len(v) - 1):
    for j in range(i+1, len(v)):
        n = 2020 - v[i] - v[j]

        if n in v[j+1:]:
            print(n * v[i] * v[j])
