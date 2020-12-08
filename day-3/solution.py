from functools import reduce


def main():
    with open('input', 'r') as f:
        world = [l for l in f.read().split('\n') if l]

    # Part 1
    print(count_trees(world, lambda x, y: (x+1, y+3)))

    # Part 2
    print(reduce(lambda x, y: x*y, [
        count_trees(world, lambda x, y: (x+1, y+1)),
        count_trees(world, lambda x, y: (x+1, y+3)),
        count_trees(world, lambda x, y: (x+1, y+5)),
        count_trees(world, lambda x, y: (x+1, y+7)),
        count_trees(world, lambda x, y: (x+2, y+1))
    ]))


def count_trees(world, slope):
    """
    Counts the trees along the given slope.

    :param world: World
    :param slope: Slope function - int, int -> int, int
    :return:
    """
    x, y = (0, 0)
    count = 0

    while True:
        x, y = slope(x, y)
        v = get_pos(x, y, world)

        if v == '#':
            count += 1

        elif v is None:
            return count


def get_pos(x, y, world):
    """
    Gets a position in the world, which expands infinitely to the right.

    :param x: Line number
    :param y: Column number
    :param world: List of lists with the same width
    :return: Element at the position, or None if past the vertical boundary
    """
    width = len(world[0])

    try:
        return world[x][y % width]
    except IndexError:
        return None


if __name__ == '__main__':
    main()
