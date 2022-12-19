def iterate_pairs_from_file(path):
    files = open(path, 'r').read().strip().split('\n')
    for line in files:
        yield tuple(map(int, line.replace(',', '-').split('-')))


def total_coverage(a1, a2, b1, b2):
    return (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2)


def partial_coverage(a1, a2, b1, b2):
    #ugly but works
    x = set(range(a1, a2 + 1))
    y = set(range(b1, b2 + 1))

    return len(x.intersection(y)) > 0


def main():
    part_1 = 0
    part_2 = 0
    for a1, a2, b1, b2 in iterate_pairs_from_file('input.txt'):
        if total_coverage(a1, a2, b1, b2):
            part_1 += 1
        if partial_coverage(a1, a2, b1, b2):
            part_2 += 1

    print("Part 1 :",part_1)
    print("Part 2 :",part_2)


if __name__ == '__main__':
    main()
