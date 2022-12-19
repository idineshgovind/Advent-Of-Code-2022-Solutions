day6 = open("input.txt", 'r')
signal = day6.read().rstrip()

signal_length = len(signal)


def p1(chars):
    i = 0

    while i < signal_length:
        string = signal[i:i + chars]

        if len(set(string)) == chars:
            return i + chars

        i += 1


print("Part 1 :", str(p1(4)))
print("Part 2 :", str(p1(14)))
