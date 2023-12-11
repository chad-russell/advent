import math
import functools

input = open(0).read().strip().splitlines()

instructions = input[0]

map = {}
for r in input[2:]:
    input, outputs = r.split(' = ')
    l, r = outputs.replace('(', '').replace(')', '').split(', ')
    map[input] = (l, r)

def count_steps(start, end):
    cur = start
    step_count = 0
    while True:
        for i in instructions:
            step_count += 1
            if i == 'L':
                cur = map[cur][0]
            else:
                cur = map[cur][1]
            if (end == 'ZZZ' and cur == 'ZZZ') or (end == 'Z' and cur[-1] == 'Z'):
                return step_count

def part1():
    answer = count_steps('AAA', 'ZZZ')
    # assert(answer == 18113)
    return answer

def part2():
    cur = [m for m in map.keys() if m[-1] == 'A']
    step_counts = [count_steps(c, 'Z') for c in cur]
    step_count = functools.reduce(math.lcm, step_counts)
    # assert(step_count == 12315788159977)
    return step_count

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
