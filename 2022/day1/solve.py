input = open(0).read().split('\n\n')

linesums = [sum([int(n) for n in line.split('\n') if n != '']) for line in input]
linesums.sort()

def part1():
    answer = linesums[-1]
    # assert(part1 == 69310)
    return answer

def part2():
    answer = sum(linesums[-3:])
    # assert(part2 == 206104)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
