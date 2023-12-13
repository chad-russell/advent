input = open(0).read().split('\n\n')

patterns = [x.splitlines() for x in input]

def rotate(p):
    return list(zip(*p[::-1]))

def find_mirror(p, target_delta):
    for row in range(1, len(p)):
        above = p[:row][::-1]
        below = p[row:]

        # zip rows in above and below, and futher zip the characters in each row
        zipped = [zip(a, b) for a, b in zip(above, below)]

        delta = sum(a != b for z in zipped for a, b in z)
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
