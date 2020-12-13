from copy import deepcopy


def main():
    with open('input', 'r') as f:
        world = [[c for c in l.strip()] for l in f.readlines() if l]

        p1_world = world
        prev = None
        while prev != p1_world:
            prev = p1_world
            p1_world = model_tick(p1_world)
        print("Part 1:", sum([len(list(filter(lambda s: s == '#', l))) for l in p1_world]))

        p2_world = world
        prev = None
        while prev != p2_world:
            prev = p2_world
            p2_world = model_tick(p2_world, version=2)
        print("Part 2:", sum([len(list(filter(lambda s: s == '#', l))) for l in p2_world]))


def model_tick(world, version=1):
    new = deepcopy(world)

    for y, row in enumerate(world):
        for x, c in enumerate(row):
            if c == '.':
                continue

            surroundings = get_surroundings(world, x, y, version)
            occupied = len(list(filter(lambda s: s == '#', surroundings)))

            if c == 'L' and occupied == 0:
                new[y][x] = '#'

            elif version == 1 and c == '#' and occupied >= 4:
                new[y][x] = 'L'

            elif version == 2 and c == '#' and occupied >= 5:
                new[y][x] = 'L'

    return new


def get_coord(world, x, y, default=None):
    if x < 0 or y < 0:
        return None

    try:
        return world[y][x]
    except IndexError:
        return default


def get_surroundings(world, x, y, version=1):
    directions = [
        (0, -1),   # N
        (1, -1),   # NE
        (1, 0),    # E
        (1, 1),    # SE
        (0, 1),    # S
        (-1, 1),   # SW
        (-1, 0),   # W
        (-1, -1),  # NW
    ]

    if version == 1:
        return [get_coord(world, x+dx, y+dy) for dx, dy in directions]

    elif version == 2:
        ret = []
        for dx, dy in directions:
            c = None
            nx = x
            ny = y
            while True:
                nx += dx
                ny += dy
                c = get_coord(world, nx, ny)
                if c != '.':
                    break
            ret.append(c)
        return ret


def print_world(world):
    for l in world:
        for c in l:
            print(c, end='')
        print()


if __name__ == '__main__':
    main()
