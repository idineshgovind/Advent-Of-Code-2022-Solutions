dirs = {'/': 0}
cd = ['/']
with open("input.txt", "r") as f:
    for l in f.readlines():
        ls = l[:-1].split(" ")
        if ls[0] == '$':
            if ls[1] == 'cd':
                if ls[2] == '..':
                    cd.pop()
                elif ls[2] == '/':
                    cd = ['/']
                else:
                    cd.append(ls[2])
        elif ls[0] == 'dir':
            dirs["".join(cd) + ls[1]] = 0
        else:
            dirs["".join(cd)] += int(ls[0])
            for i in range(1, len(cd)):
                dirs["".join(cd[:-i])] += int(ls[0])
print("Part 1 :", sum(v for v in dirs.values() if v <= 100000))
print("Part 2 :", min(v for v in dirs.values() if v >= dirs['/'] - 40000000))
