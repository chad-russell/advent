import re

input = open(0).read().strip().splitlines()

def get_possible_part_nums(row):
    allmatches = []
    rowmatches = re.finditer(r'([\d]+)', row)
    for match in rowmatches:
        allmatches.append((match.start(), match.end()))
    return allmatches

def get_possible_gears(row):
    allmatches = []
    rowmatches = re.finditer(r'(\*)', row)
    for match in rowmatches:
        allmatches.append((match.start()))
    return allmatches

def isspecial(ch):
    return ch != '.' and ch != '\n' and not ch.isalpha()

def is_part_number(pn, row, input):
    height = len(input)
    width = len(input[0])

    cs = pn[0]
    ce = pn[1]

    for rn in [row - 1, row + 1]:
        for cn in range(cs - 1, ce + 1):
            if rn >= 0 and rn < height and cn >= 0 and cn < width:
                if isspecial(input[rn][cn]):
                    return True
    for cn in [cs - 1, ce]:
        if cn >= 0 and cn < width:
            if isspecial(input[row][cn]):
                return True

    return False

def adjacent(gr, g, pnr, pn):
    if gr == pnr and (g == pn[0] - 1 or g == pn[1]):
        return True
    if (gr == pnr - 1 or gr == pnr + 1) and (g >= pn[0] - 1 and g <= pn[1]):
        return True
    return False

def part1():
    possible_part_nums = [get_possible_part_nums(row) for row in input]
    sum = 0
    for row, pns in enumerate(possible_part_nums):
        for pn in pns:
            if is_part_number(pn, row, input):
                sum += int(input[row][pn[0]:pn[1]])

    # assert(sum == 539433)
    return sum

def part2():
    possible_part_nums = [get_possible_part_nums(row) for row in input]
    possible_gears = [get_possible_gears(row) for row in input]

    gear_ratio_sum = 0
    for gr, gs in enumerate(possible_gears):
        for g in gs:
            num_adjacent_parts = 0
            gear_ratio = 1
            for pnr in range(gr - 1, gr + 2):
                for pn in possible_part_nums[pnr]:
                    if adjacent(gr, g, pnr, pn):
                        num_adjacent_parts += 1
                        gear_ratio *= int(input[pnr][pn[0]:pn[1]])
            if num_adjacent_parts == 2:
                gear_ratio_sum += gear_ratio

    # assert(gear_ratio_sum == 75847567)
    return gear_ratio_sum


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
