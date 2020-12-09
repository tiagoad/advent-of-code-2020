import itertools

PREVIOUS_N = 25


def main():
    with open('input', 'r') as f:

        numbers = list(map(int, itertools.islice(f, PREVIOUS_N)))
        for line in f:
            n = int(line)

            if not sum_of_two(n, numbers[-PREVIOUS_N:]):
                print("Part 1:", n)

                summed_range = find_sum_range(n, numbers)
                print("Part 2:", min(summed_range) + max(summed_range))
                return

            numbers.append(n)


def sum_of_two(n, lst):
    for i, a in enumerate(lst):
        for b in lst[i+1:]:
            if a + b == n:
                return True
    return False


def find_sum_range(n, lst):
    for i, a in enumerate(lst):
        summed = a
        summed_numbers = [a]
        for b in lst[i+1:]:
            summed += b
            summed_numbers.append(b)

            if summed == n:
                return summed_numbers

    return None


if __name__ == '__main__':
    main()
