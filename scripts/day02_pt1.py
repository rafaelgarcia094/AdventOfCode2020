import re

r = 0

for _ in range(1000):
    min_count, max_count, letter, _, password = re.split(r'\W', input())

    if int(min_count) <= password.count(letter) <= int(max_count):
        r += 1

print(r)
