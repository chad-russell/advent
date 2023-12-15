input = open(0).read().splitlines()
input = [list(row) for row in input]

def move_rock(src_ri, src_ci, dst_ri, dst_ci):
    input[dst_ri][dst_ci] = 'O'
    input[src_ri][src_ci] = '.'

def load_factor(ri):
    return len(input) - ri

def num_rocks(row):
    return sum(ch == 'O' for ch in row)

def calculate_load():
    return sum(load_factor(ri) * num_rocks(row) for ri, row in enumerate(input))

def roll_north(ri, ci):
    if input[ri][ci] != 'O':
        return
    stopping_point = (n for n in range(ri - 1, -1, -1) if input[n][ci] != '.')
    stopping_point = next(stopping_point, -1) + 1
    if stopping_point != ri:
        move_rock(ri, ci, stopping_point, ci)

def roll_all_north():
    for ri in range(len(input)):
        for ci in range(len(input[0])):
            roll_north(ri, ci)

def rotate():
    global input
    input = [''.join(row) for row in input]
    flipped = zip(*input[::-1])
    input = [list(row) for row in flipped]

def spin_cycle():
    for _ in range(4):
        roll_all_north()
        rotate()

def part1():
    for ri in range(len(input)):
        for ci in range(len(input[0])):
            roll_north(ri, ci)

    answer = calculate_load()

    # assert(load == 113486)

    return answer

def part2():
    nloads = 150
    loads = []
    for _ in range(nloads):
        spin_cycle()
        loads.append(calculate_load())

    start = 100
    min_cycle_len = 10

    pat = loads[start:start + min_cycle_len]
    seek_range = range(start + min_cycle_len + 1, nloads - 1 - min_cycle_len)

    cycle_len = next(i - start for i in seek_range if loads[i:i + min_cycle_len] == pat)
    remainder = (1_000_000_000 - start) % cycle_len
    answer = loads[start + remainder - 1]

    # assert(answer == 104409)

    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
