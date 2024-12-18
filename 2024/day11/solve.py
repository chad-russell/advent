input = open(0).read().strip().split(' ')

def add_to_stone_set(stones, key, value):
    if key in stones:
        stones[key] += value
    else:
        stones[key] = value

def blink(stones):
    new_stones = dict()
    for stone, count in stones.items():
        if stone == '0':
            add_to_stone_set(new_stones, '1', count)
        elif len(stone) % 2 == 0:
            add_to_stone_set(new_stones, str(int(stone[:len(stone) // 2])), count)
            add_to_stone_set(new_stones, str(int(stone[len(stone) // 2:])), count)
        else:
            add_to_stone_set(new_stones, str(int(stone) * 2024), count)
    return new_stones

def solve(n):
    stones = dict({s: 1 for s in input})
    for _ in range(n):
        stones = blink(stones)
    return sum(stones.values())

def part1():
    return solve(25)
            
def part2():
    return solve(75)

print(f'part 1: {part1()}') # 183435
print(f'part 2: {part2()}') # 218279375708592
