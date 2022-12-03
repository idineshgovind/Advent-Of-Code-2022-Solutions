with open('input.txt', 'r') as f:
    data = [line.strip().replace(' ', '') for line in f]

part1 = sum({'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}[round] for round in data)
part2 = sum({'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}[round] for round in data)

print("PART 1 :",part1)
print("PART 2 :",part2)