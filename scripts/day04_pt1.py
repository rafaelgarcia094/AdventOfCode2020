def create_dict(attr):
    return {a: False for a in attr}


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

d = create_dict(fields)
valid_passports = 0
valid_fields = 0

for _ in range(1138):
    line = input()

    if len(line) == 0:
        if valid_fields == len(fields):
            valid_passports += 1

        d = create_dict(fields)
        valid_fields = 0

        continue

    for field in line.split(' '):
        name = field.split(':')[0]

        if name != 'cid' and not d[name]:
            d[name] = True
            valid_fields += 1

print(valid_passports)
