input = open(0).read().strip().splitlines()

parsed = [[list(map(int, p.split('-'))) for p in row.split(',')] for row in input]

def fully_contains(a, b):
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])

def overlaps(a, b):
    return (a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1]) or (a[0] <= b[0] and a[1] >= b[1])

def part1():
    answer = sum(fully_contains(a, b) for a, b in parsed)
    # assert(answer == 538
    return answer

def part2():
    answer = sum(overlaps(a, b) for a, b in parsed)
    # assert(answer == 792)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
