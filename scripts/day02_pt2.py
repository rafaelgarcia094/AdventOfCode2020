import re

r = 0

for _ in range(1000):
    idx1, idx2, letter, _, password = re.split(r'\W', input())
    is_letter1 = password[int(idx1) - 1] == letter
    is_letter2 = password[int(idx2) - 1] == letter

    if is_letter1 ^ is_letter2:
        r += 1

print(r)
