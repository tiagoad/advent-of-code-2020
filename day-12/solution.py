import math


def main():
    with open('input', 'r') as f:
        commands = [(c[0], int(c[1:])) for c in [l.strip() for l in f.readlines() if l]]

    x, y = part1(commands)
    print("Part 1:", abs(x)+abs(y))

    x, y = part2(commands, (10, 1))
    print("Part 2:", abs(x)+abs(y))


def part1(commands):
    x, y, a = 0, 0, 0

    for c, n in commands:
        if c == 'N':
            y += n
        elif c == 'S':
            y -= n
        elif c == 'E':
            x += n
        elif c == 'W':
            x -= n
        elif c == 'L':
            a += n
        elif c == 'R':
            a -= n
        elif c == 'F':
            r = math.radians(a)
            x += int(math.cos(r)) * n
            y += int(math.sin(r)) * n

    return x, y


def part2(commands, initial_waypoint):
    sx, sy = 0, 0  # ship
    wx, wy = initial_waypoint

    for c, n in commands:
        if c == 'N':
            wy += n
        elif c == 'S':
            wy -= n
        elif c == 'E':
            wx += n
        elif c == 'W':
            wx -= n
        elif c == 'L' or c == 'R':
            r = math.radians(n if c == 'L' else -n)
            wx, wy = wx * int(math.cos(r)) - wy * int(math.sin(r)), wy * int(math.cos(r)) + wx * int(math.sin(r))
        elif c == 'F':
            sx += wx * n
            sy += wy * n

    return sx, sy


if __name__ == '__main__':
    main()
