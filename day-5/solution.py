import bisect

START_RANGE = (0, 127, 0, 7)


def main():
    with open('input', 'r') as f:
        r1, r2, c1, c2 = START_RANGE
        max_sid = -1
        sids = []

        while True:
            c = f.read(1)

            # EOF
            if c == '':
                break

            # rows - keep upper half
            elif c == 'F':
                r2 -= (r2 - r1 + 1) // 2

            # rows - keep lower half
            elif c == 'B':
                r1 += (r2 - r1 + 1) // 2

            # cols - keep upper half
            elif c == 'L':
                c2 -= (c2 - c1 + 1) // 2

            # cols - keep lower half
            elif c == 'R':
                c1 += (c2 - c1 + 1) // 2

            # end of line
            elif c == "\n":
                row = r1
                col = c1
                sid = row * 8 + col

                if sid > max_sid:
                    max_sid = sid

                # insert into sorted list
                bisect.insort(sids, sid)

                r1, r2, c1, c2 = START_RANGE

        # Part 1 - Look for the highest seat ID
        print("Maximum SID:", max_sid)

        # Part 2 - Look for missing seat
        for i, sid in enumerate(sids):
            if sids[i - 1] == sid - 2:
                print("Missing SID:", sid-1)
                break


if __name__ == '__main__':
    main()
