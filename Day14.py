import bresenham

inp = [[tuple(map(int,c.split(","))) for c in line.strip().split(" -> ")] for line in open("input.txt").readlines()]

obstructions = {}
for struct in inp:
    coord = struct[0]
    for i in range(1, len(struct)):
        for e in bresenham.bresenham(coord[0], coord[1], struct[i][0], struct[i][1]):
            obstructions[(e[0]+1j*e[1])] = 1
        coord = struct[i]

sandsource = 500+0j

def simsand(spos):
    if (sandpos + 1j not in obstructions):
        return sandpos + 1j, True
    else:
        # Down and to the left
        if (sandpos + (-1+1j)) not in obstructions:
            return sandpos + (-1+1j), True
        elif (sandpos + (1+1j)) not in obstructions:
            return sandpos + (1+1j), True
    return 0+0j, False


abyss = max([k.imag for k in obstructions.keys()])

working = True
while (working):
    sandpos = sandsource

    while True:
        if (sandpos.imag > abyss):
            working = False
            break
        sandpos_new, succ = simsand(sandpos)
        if (not succ):
            obstructions[sandpos] = 2
            break
        else:
            sandpos = sandpos_new
    # break

print(f"Part 1 : {sum([v==2 for v in obstructions.values()])}")

abyss = max([k.imag for k in obstructions.keys()]) + 2

for i in range(-10000, 10000):
    obstructions[i+1j*abyss] = 1

working = True
while (working):
    sandpos = sandsource

    while True:
        if (sandpos.imag > abyss):
            working = False
            break
        sandpos_new, succ = simsand(sandpos)
        if (not succ):
            obstructions[sandpos] = 2
            break
        else:
            sandpos = sandpos_new
    # break
    if (sandpos == 500+0j): break

print(f"Part 2 : {sum([v==2 for v in obstructions.values()])}")