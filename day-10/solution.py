def main():
    with open('input', 'r') as f:
        adapters = sorted(map(int, f.read().strip().split('\n')))
        adapters.append(max(adapters) + 3)

        diffs = get_differences(adapters)
        print("Part 1:", diffs[1] * diffs[3])

        print("Part 2:", get_arrangements(adapters))


def get_differences(adapters):
    diffs = {}
    prev = 0
    for curr in adapters:
        diffs[curr - prev] = diffs.get(curr - prev, 0) + 1
        prev = curr
    return diffs


def get_arrangements(adapters):
    adapters = adapters.copy()
    adapters.insert(0, 0)

    memo = {}

    def get_under(a):
        if a == adapters[-1]:
            return 1

        v = 0
        for i in range(a + 1, a + 4):
            if i in adapters:
                res = memo.get(i)
                if res:
                    v += res
                else:
                    res = get_under(i)
                    v += res
                    memo[i] = res
        return v

    return get_under(adapters[0])


if __name__ == '__main__':
    main()
