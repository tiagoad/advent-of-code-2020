import re


def main():
    # Turn input into a dictionary like:
    # {
    #   'shiny gold': [(2, 'dark red')],
    #   'dark red': [(2, 'orange'), (1, 'red')]
    # }
    colors = {}
    with open('input', 'r') as f:
        for l in f:
            out_colour, in_colours = re.match(r'^(.+?) bags contain (.+)\.$', l).groups()
            in_colours = [re.match(r'(\d+) (.+) bags?', c).groups() for c in in_colours.split(', ') if c != 'no other bags']
            in_colours = [(int(n), c) for n, c in in_colours]
            colors[out_colour] = in_colours

    # Part 1 - How many colours eventually have "shiny gold" inside?
    print("Part 1:", sum(['shiny gold' in colors_inside(c, colors) for c in colors.keys()]))

    # Part 2 - How many bags are inside shiny gold?
    print("Part 2:", bags_inside('shiny gold', colors))


def colors_inside(color, colors):
    """Returns a set of colours that are eventually inside the color"""
    ret = set()
    for n, c in colors[color]:
        ret.add(c)
        ret.update(colors_inside(c, colors))
    return ret


def bags_inside(color, colors):
    """Returns the number of bags inside a given color"""
    return sum([n + n * bags_inside(c, colors) for n, c in colors[color]])


if __name__ == '__main__':
    main()
