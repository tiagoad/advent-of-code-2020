import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def main():
    with open('input', 'r') as f:
        passports = [p.strip() for p in f.read().split('\n\n') if p]

    count_p1 = 0
    count_p2 = 0
    for p in passports:
        args = {k: v for k, v in [a.split(':') for a in re.split(r'\s+', p)]}

        if is_valid_v1(args):
            count_p1 += 1

        if is_valid_v2(args):
            count_p2 += 1

    print(count_p1)
    print(count_p2)


def is_valid_v1(data):
    return not any([data.get(f) is None for f in REQUIRED_FIELDS])


def is_valid_v2(data):
    if not is_valid_v1(data):
        return False

    for k, v in data.items():
        # four digits
        if k in ['byr', 'iyr', 'eyr']:
            if not re.match(r'\d\d\d\d$', v):
                return False
            v = int(v)

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if k == 'byr':
            if v < 1920 or v > 2002:
                return False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if k == 'iyr':
            if v < 2010 or v > 2020:
                return False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if k == 'eyr':
            if v < 2020 or v > 2030:
                return False

        # hgt (Height) - a number followed by either cm or in:
        #   If cm, the number must be at least 150 and at most 193.
        #   If in, the number must be at least 59 and at most 76.
        if k == 'hgt':
            m = re.match(r'(\d+)(cm|in)$', v)
            if not m:
                return False

            h, unit = m.groups()
            h = int(h)

            if not ((unit == 'cm' and 150 <= h <= 193) or (unit == 'in' and 59 <= h <= 76)):
                return False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if k == 'hcl':
            if not re.match(r'#[0-9a-f]{6}$', v):
                return False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if k == 'pid':
            if not re.match(r'\d{9}$', v):
                return False

    return True


if __name__ == '__main__':
    main()
