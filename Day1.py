first, second, third = 0, 0, 0
elf_calories = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line != '':
            elf_calories += int(line)
            continue
        if elf_calories >= first:
            third = second
            second = first
            first = elf_calories
        elif elf_calories >= second:
            third = second
            second = elf_calories
        elif elf_calories >= third:
            third = elf_calories
        elf_calories = 0

    print("Part 1 :",first)
    print("Part 2 :",first + second + third)
