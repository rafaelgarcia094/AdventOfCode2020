import re


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
        name, value = field.split(':')

        if name != 'cid' and not d[name]:
            d[name] = True

            if name == 'byr' and len(value) == 4 and 1920 <= int(value) <= 2002:
                valid_fields += 1
            if name == 'iyr' and len(value) == 4 and 2010 <= int(value) <= 2020:
                valid_fields += 1
            if name == 'eyr' and len(value) == 4 and 2020 <= int(value) <= 2030:
                valid_fields += 1
            if name == 'hgt':
                if value[-2:] == 'cm' and len(value) == 5 and 150 <= int(value[:3]) <= 193:
                    valid_fields += 1
                if value[-2:] == 'in' and len(value) == 4 and 59 <= int(value[:2]) <= 76:
                    valid_fields += 1
            if name == 'hcl' and re.match(r'#(\d|[a-f]){6}$', value):
                valid_fields += 1
            if name == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid_fields += 1
            if name == 'pid' and re.match(r'(\d){9}$', value):
                valid_fields += 1

print(valid_passports)
