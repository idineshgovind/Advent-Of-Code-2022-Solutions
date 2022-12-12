import re
from dataclasses import dataclass
from functools import partial
from typing import Callable
import math


@dataclass
class Monkey:
    items: list[int]
    op: str
    divisor: int
    condition_true: int
    condition_false: int
    count: int = 0


@dataclass
class Data:
    monkeys: list[Monkey]
    lcm: int


PassItem = list[tuple[int, int]]
TurnFunc = Callable[[Monkey, int, int], PassItem]


def parse_input(filename: str) -> Data:
    with open(filename) as f:
        monkeys = [chunk.splitlines() for chunk in f.read().split('\n\n')]

    res = []
    for monkey in monkeys:
        data = [line.strip() for line in monkey[1:]]

        items = [int(n) for n in re.findall('\d+', data[0])]
        op = data[1].split(' = ')[-1]
        divisor = int(re.findall('\d+', data[2])[0])
        condition_true = int(re.findall('\d+', data[3])[0])
        condition_false = int(re.findall('\d+', data[4])[0])

        res.append(Monkey(items, op, divisor, condition_true, condition_false))

    """
    Find the least common multiple of all divisors
    This allows modular arithmetic to reduce the size of the numbers
    Unchecked (or without floor division by 3) the numbers would grow exponentially
    """
    lcm = math.lcm(*[monkey.divisor for monkey in res])
    return Data(res, lcm)


def turn(
        monkey: Monkey,
        lcm: int,
        divisor: int = 3
) -> PassItem:
    res = []
    while monkey.items:
        old = monkey.items.pop(0)
        new = eval(monkey.op) % lcm // divisor
        if new % monkey.divisor == 0:
            res.append((monkey.condition_true, new))
        else:
            res.append((monkey.condition_false, new))

    monkey.count += len(res)
    return res


def round(
        monkeys: list[Monkey],
        turn_func: TurnFunc
) -> list[Monkey]:
    for i, monkey in enumerate(monkeys):
        if not (pass_data := turn_func(monkey)):
            continue
        for pass_to_monkey, item in pass_data:
            monkeys[pass_to_monkey].items.append(item)

    return monkeys


def run(
        filename: str,
        divisor: int = 3,
        rounds: int = 20,
        print_rounds=False
) -> int:
    A = parse_input(filename)
    turn_func = partial(turn, lcm=A.lcm, divisor=divisor)

    for i in range(rounds):
        A.monkeys = round(A.monkeys, turn_func)

    first, second = sorted([monkey.count for monkey in A.monkeys], reverse=True)[:2]
    return first * second


part1 = partial(run, divisor=3, rounds=20)
part2 = partial(run, divisor=1, rounds=10_000)

print("Part 1:", part1('input.txt'))
print("Part 2:", part2('input.txt'))
