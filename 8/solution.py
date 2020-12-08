import copy


def main():
    with open('input', 'r') as f:
        code = [l.strip().split(' ') for l in f.read().splitlines()]

    pc, acc = find_loop(code)
    print("Part 1:", acc)

    for i, (inst, arg) in enumerate(code):
        if inst == 'jmp' or inst == 'nop':
            new = copy.deepcopy(code)
            new[i][0] = 'jmp' if inst == 'nop' else 'nop'

            pc, acc = find_loop(new)
            if pc is None:
                print("Part 2:", acc)
                break


def find_loop(code):
    hits = [0 for i in range(len(code))]
    pc = 0
    acc = 0
    while True:
        if pc == len(code):
            return None, acc
        hits[pc] += 1
        if hits[pc] > 1:
            return pc, acc

        inst, arg = code[pc]

        if inst == 'jmp':
            pc += int(arg)

        elif inst == 'acc':
            acc += int(arg)
            pc += 1

        elif inst == 'nop':
            pc += 1


if __name__ == '__main__':
    main()
