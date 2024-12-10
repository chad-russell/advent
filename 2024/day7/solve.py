input = [(int(target), list(map(int, nums.strip().split(' ')))) for target, nums in map(lambda e: e.split(':'), open(0).read().splitlines())]

def greedy_try(target, p, nums, allow_concat=False):
    if len(nums) == 0:
        return p == target
    if p > target:
        return False
    return greedy_try(target, p + nums[0], nums[1:], allow_concat=allow_concat) \
        or greedy_try(target, p * nums[0], nums[1:], allow_concat=allow_concat) \
        or (allow_concat and greedy_try(target, int(str(p) + str(nums[0])), nums[1:], allow_concat=allow_concat))

def part1():
    return sum(target for target, nums in input if greedy_try(target, nums[0], nums[1:]))

def part2():
    return sum(target for target, nums in input if greedy_try(target, nums[0], nums[1:], allow_concat=True))

print(f'part 1: {part1()}') # 6231007345478
print(f'part 2: {part2()}') # 333027885676693
