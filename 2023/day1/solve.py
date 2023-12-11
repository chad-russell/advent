input = open(0).read().strip().splitlines()

def part1():
    sum = 0
    for line in input:
        c1 = -1
        c2 = -1
        for ch in line:
            if ch.isdigit():
                dig = int(ch)
                if c1 == -1:
                    c1 = dig
                c2 = dig
        sum += 10 * c1 + c2
    # assert(sum == 54667)
    return sum


def part2():
    sum = 0
    for line in input:
        c1 = 0
        c2 = 0
        found_digit = False

        for i in range(0, len(line)):
            ch = line[i]
            digit = 0
            found = False

            if ch.isdigit():
                digit = int(ch)
                found = True
            else:
                ss = line[i:]
                if ss.startswith('one'):
                    digit = 1
                    found = True
                elif ss.startswith('two'):
                    digit = 2
                    found = True
                elif ss.startswith('three'):
                    digit = 3
                    found = True
                elif ss.startswith('four'):
                    digit = 4
                    found = True
                elif ss.startswith('five'):
                    digit = 5
                    found = True
                elif ss.startswith('six'):
                    digit = 6
                    found = True
                elif ss.startswith('seven'):
                    digit = 7
                    found = True
                elif ss.startswith('eight'):
                    digit = 8
                    found = True
                elif ss.startswith('nine'):
                    digit = 9
                    found = True

            if found:
                if not found_digit:
                    c1 = digit
                    found_digit = True
                c2 = digit

        sum += 10 * c1 + c2
    # assert(sum == 54203)
    return sum


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
