input = [list(map(int, i.split())) for i in open(0).read().strip().splitlines()]


def is_safe(mr):
    return all(r <= -1 and r >= -3 for r in mr) or all(r >= 1 and r <= 3 for r in mr)

def diff(row):
    return [b - a for a, b in zip(row, row[1:])]

def part1():
    return sum(is_safe(diff(row)) for row in input)


def gen_alts(row):
    return [diff(row[:i] + row[i+1:]) for i in range(0, len(row))]

def part2():
    return sum(any(is_safe(alt) for alt in gen_alts(r)) for r in input)

print(f'part 1: {part1()}') # 326
print(f'part 2: {part2()}') # 381
