input = [list(map(int, i.split())) for i in open(0).read().strip().splitlines()]

def part1():
    left = sorted(l for l, _ in input)
    right = sorted(r for _, r in input)
    return sum(abs(l - r) for l, r in zip(left, right))

def part2():
    right = dict[int, int]((r, 0) for _, r in input)
    for _, r in input:
        right[r] += 1
    return sum(l * (right.get(l) or 0) for l, _ in input)



print(f'part 1: {part1()}') # 1590491
print(f'part 2: {part2()}') # 22588371
