import sys
sys.setrecursionlimit(10_000)

input = open(0).read().splitlines()

steps = 0

visited = []

def pos_in_bounds(pos):
    r, c = pos
    return r >= 0 and c >= 0 \
            and r < len(input) and c < len(input[0]) \
            and input[r][c] in '.<>^v' \
            and (r, c) not in visited

def in_bounds(ps):
    return tuple([p for p in ps if pos_in_bounds(p)])

def options_p1(pos):
    r, c = pos

    if input[r][c] == '>':
        return in_bounds([(r, c+1)])
    if input[r][c] == '<':
        return in_bounds([(r, c-1)])
    if input[r][c] == '^':
        return in_bounds([(r-1, c)])
    if input[r][c] == 'v':
        return in_bounds([(r+1, c)])

    return in_bounds([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

def options_p2(pos):
    r, c = pos
    return in_bounds([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

def print_input():
    for line in input:
        print(line)
    print('\n')

max_step_size = 0

def step_p1(p, steps):
    global max_step_size

    if p == (len(input) - 1, len(input[0]) - 2):
        max_step_size = max(max_step_size, steps)
        return

    for o in options_p1(p):
        visited.append(o)
        step_p1(o, steps + 1) 
        assert(visited[-1] == o)
        visited.pop()

def step_p2(p, steps):
    global max_step_size

    if p == (len(input) - 1, len(input[0]) - 2):
        max_step_size = max(max_step_size, steps)
        return

    for o in options_p2(p):
        visited.append(o)
        step_p2(o, steps + 1) 
        assert(visited[-1] == o)
        visited.pop()

def part1():
    visited.append((0, 1))
    step_p1((0, 1), 0)
    return max_step_size

def part2():
    nodes = 

# print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
