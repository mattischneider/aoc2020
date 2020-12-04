import re

FILE = "04.txt"

COUNTRY_ID_KEY = 'cid'
KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open(FILE, 'r') as f:
    passports = f.read().split('\n\n')
    passports = [p.replace('\n', ' ').split(' ') for p in passports]
    passports = [dict(s.split(':') for s in p) for p in passports]


def is_valid_passport_first_part(passport):
    if len(passport) <= 6:
        return False
    if COUNTRY_ID_KEY not in passport and len(passport) == len(KEYS):
        return True
    for key in KEYS:
        if key not in passport:
            return False
    return True


# first part
print(sum([is_valid_passport_first_part(p) for p in passports]))


def is_valid_passport_second_part(passport):
    for key in KEYS:
        if key not in passport:
            return False
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if passport['hgt'][-2:] not in ['cm', 'in']:
        return False
    if passport['hgt'][-2:] == 'cm' and not (150 <= int(passport['hgt'].replace('cm', '')) <= 193):
        return False
    if passport['hgt'][-2:] == 'in' and not (59 <= int(passport['hgt'].replace('in', '')) <= 76):
        return False
    if passport['hcl'][0] != '#' or re.compile('^[0-9a-f]{6}$').match(passport['hcl'][1:]) is None:
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if re.compile('^[0-9]{9}$').match(passport['pid']) is None:
        return False
    return True


# second part
print(sum([is_valid_passport_second_part(p) for p in passports]))
