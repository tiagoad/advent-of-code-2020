def main():
    with open('input', 'r') as f:
        lines = f.readlines()
        arrival = int(lines[0])
        buses = [int(bid) if bid != 'x' else None for bid in lines[1].split(',')]

        # Part 1
        min_bid, min_time = next_bus(arrival, buses)
        print("Part 1:", min_bid*min_time)

        # Part 2
        t = alignment_timestamp(buses)
        print("Part 2:", t)


def next_bus(arrival, buses):
    min_bid, min_time = None, None
    for bid in buses:
        if bid is None:
            continue

        time_until = bid - arrival % bid
        if min_time is None or min_time > time_until:
            min_bid, min_time = bid, time_until
    return min_bid, min_time


def alignment_timestamp(buses):
    t = 0
    cycle = 1

    for bi, bid in enumerate(buses):
        if bid is None:
            continue

        while True:
            if (t + bi) % bid == 0:
                break
            t += cycle

        cycle *= bid

    return t


if __name__ == '__main__':
    main()
