def main():
    with open('input', 'r') as f:
        numbers = [int(l) for l in f.read().split('\n') if l]

    a, b = find_sum(numbers, 2020)
    print(a*b)

    a, b, c = find_sum_three(numbers, 2020)
    print(a*b*c)


def find_sum(numbers, target):
    for i, a in enumerate(numbers):
        for b in numbers[i:]:
            if a + b == target:
                return (a, b)

    return None


def find_sum_three(numbers, target):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i:]):
            for c in numbers[j:]:
                if a + b + c == target:
                    return (a, b, c)

    return None


if __name__ == '__main__':
    main()
