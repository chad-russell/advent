import copy

input = open(0).read().splitlines()

def parse_coord(xyz):
    return tuple(map(int, xyz.split(',')))

def sorted_inclusive_range(n):
    return range(min(n), max(n) + 1)

bricks = []
for line in input:
    start, end = map(parse_coord, line.split('~'))
    bricks.append(list(map(sorted_inclusive_range, zip(start, end))))

min_z = min(b[2][0] for b in bricks)
max_z = max(b[2][-1] for b in bricks)

min_y = min(b[1][0] for b in bricks)
max_y = max(b[1][-1] for b in bricks)

min_x = min(b[0][0] for b in bricks)
max_x = max(b[0][-1] for b in bricks)

bricks.sort(key=lambda n: n[2][0])

def occupied(x, y, z, bn, ignore_list):
    if z <= 0:
        return True

    for bn in range(bn - 1, max(bn - 200, 0), -1):
        if bn in ignore_list:
            continue
        bx, by, bz = bricks[bn]
        if x in bx and y in by and z in bz:
            return True

    return False

def try_fall(bn, ignore_list=[]):
    bx, by, bz = bricks[bn]

    can_fall = True
    can_fall_amount = 0

    while can_fall:
        can_fall_amount += 1
        for z in bz:
            for y in by:
                for x in bx:
                    if occupied(x, y, z - can_fall_amount, bn, [*ignore_list, bn]):
                        can_fall = False
    can_fall_amount -= 1
    return can_fall_amount

def can_fall_any(bn, ignore_list=[]):
    bx, by, bz = bricks[bn]

    can_fall_amount = 0

    for z in bz:
        for y in by:
            for x in bx:
                if occupied(x, y, z - can_fall_amount, bn, [*ignore_list, bn]):
                    return False

    return True

for bn in range(len(bricks)):
    can_fall_amount = try_fall(bn)
    if can_fall_amount > 0:
        bnr = bricks[bn][2]
        bricks[bn][2] = range(bnr[0] - can_fall_amount, bnr[-1] - can_fall_amount + 1)

def is_safe_to_disintigrate(dbn):
    for bn in range(len(bricks)):
        if bn == dbn:
            continue
        if bricks[bn][2][-1] <= bricks[dbn][2][0]:
            continue
        elif try_fall(bn, ignore_list=[dbn]) > 0:
            return False
    return True

def chain_reaction(dbn):
    global bricks

    bricks_copy = copy.deepcopy(bricks)

    bricks.pop(dbn)

    num_did_fall = 0
    for bn in range(len(bricks)):
        can_fall_amount = try_fall(bn)
        if can_fall_amount > 0:
            num_did_fall += 1
            bnr = bricks[bn][2]
            bricks[bn][2] = range(bnr[0] - can_fall_amount, bnr[-1] - can_fall_amount + 1)

    bricks = bricks_copy

    return num_did_fall

def part1():
    answer = sum(is_safe_to_disintigrate(bn) for bn in range(len(bricks)))
    assert(answer == 389)
    return answer

def part2():
    answer = sum(chain_reaction(bn) for bn in range(len(bricks)))
    assert(answer == 70609)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
