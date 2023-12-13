input = open(0).read().split('\n\n')
patterns = list(map(lambda x: x.splitlines(), input))

def rotate(p):
    return [[r[c] for r in p[::-1]] for c in range(len(p[0]))]

def find_mirror(p, target_delta):
    for row in range(1, len(p)):
        delta = 0
        lower = row - 1
        upper = row
        while lower >= 0 and upper < len(p):
            delta += sum(a != b for a, b in zip(p[lower], p[upper]))
            lower -= 1
            upper += 1
        if delta == target_delta:
            return row
    return 0

def helper(target_delta):
    return sum(100 * find_mirror(p, target_delta) + find_mirror(rotate(p), target_delta) for p in patterns)

def part1():
    answer = helper(0)
    # assert(answer == 30705)
    return answer

def part2():
    answer = helper(1)
    # assert(answer == 44615)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
