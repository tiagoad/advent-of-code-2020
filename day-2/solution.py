def main():
    with open('input') as f:
        lines = [l.split(': ') for l in f.read().split('\n') if l]

    # Part 1
    valid = sum([check_rule(l, rule) for rule, l in lines])
    print(valid)

    # Part 2
    valid = sum([check_rule_v2(l, rule) for rule, l in lines])
    print(valid)


def check_rule(s, rule):
    interval, letter = rule.split(' ')
    min_count, max_count = [int(n) for n in interval.split('-')]
    count = len([c for c in s if c == letter])

    return min_count <= count <= max_count


def check_rule_v2(s, rule):
    interval, letter = rule.split(' ')
    pos_a, pos_b = [int(n) for n in interval.split('-')]
    count = len([c for c in s if c == letter])

    return (s[pos_a - 1] == letter and s[pos_b - 1] != letter) \
        or (s[pos_a - 1] != letter and s[pos_b - 1] == letter)


if __name__ == '__main__':
    main()
