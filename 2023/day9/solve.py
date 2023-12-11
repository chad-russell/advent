input = open(0).read().splitlines()

def create_difflist(nums):
    diffs = [nums]
    while any(diffs[-1]):
        newdiff = [(diffs[-1][i + 1] - diffs[-1][i]) for i in range(len(diffs[-1]) - 1)]
        diffs.append(newdiff)
    return diffs

def extrapolate(nums):
    diffs = create_difflist(nums)
    diffs[-1].append(0)
    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])
    return diffs[0][-1]

def extrapolate_backward(nums):
    diffs = create_difflist(nums)
    diffs[-1].append(0)
    for i in range(len(diffs) - 2, -1, -1):
        diffs[i] = [diffs[i][0] - diffs[i + 1][0]] + diffs[i]
    return diffs[0][0]

def part1():
    sum = 0
    for l in input:
        nums = list(map(int, l.split()))
        sum += extrapolate(nums)
    # assert(sum == 1938800261)
    return sum

def part2():
    sum = 0
    for l in input:
        nums = list(map(int, l.split()))
        sum += extrapolate_backward(nums)
    # assert(sum == 1938800261)
    return sum

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')

