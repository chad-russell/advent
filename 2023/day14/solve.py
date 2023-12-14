input = list(map(list, open(0).read().splitlines()))

nrows = len(input)
ncols = len(input[0])

def move_rock(src_ri, src_ci, dst_ri, dst_ci):
    input[dst_ri][dst_ci] = 'O'
    input[src_ri][src_ci] = '.'

def load_factor(ri):
    return nrows - ri

def num_rocks(row):
    return sum(ch == 'O' for ch in row)

def roll_north(ri, ci):
    if input[ri][ci] != 'O':
        return
    stopping_point = (n for n in range(ri - 1, -1, -1) if input[n][ci] != '.')
    stopping_point = next(stopping_point, -1) + 1
    if stopping_point != ri:
        move_rock(ri, ci, stopping_point, ci)

def roll_south(ri, ci):
    if input[ri][ci] != 'O':
        return
    stopping_point = (n for n in range(ri + 1, nrows, 1) if input[n][ci] != '.')
    stopping_point = next(stopping_point, nrows) - 1
    if stopping_point != ri:
        move_rock(ri, ci, stopping_point, ci)

def roll_west(ri, ci):
    if input[ri][ci] != 'O':
        return
    stopping_point = (n for n in range(ci - 1, -1, -1) if input[ri][n] != '.')
    stopping_point = next(stopping_point, -1) + 1
    if stopping_point != ci:
        move_rock(ri, ci, ri, stopping_point)

def roll_east(ri, ci):
    if input[ri][ci] != 'O':
        return
    stopping_point = (n for n in range(ci + 1, ncols, 1) if input[ri][n] != '.')
    stopping_point = next(stopping_point, ncols) - 1
    if stopping_point != ci:
        move_rock(ri, ci, ri, stopping_point)

def calculate_load():
    return sum(load_factor(ri) * num_rocks(row) for ri, row in enumerate(input))

def part1():
    for ri, row in enumerate(input):
        for ci in range(len(row)):
            roll_north(ri, ci)

    answer = calculate_load()
    # assert(load == 113486)
    return answer

def print_input():
    for row in input:
        print(''.join(row))
    print('')

def cycle():
    for ri in range(nrows):
        for ci in range(ncols):
            roll_north(ri, ci)

    for ci in range(ncols):
        for ri in range(nrows):
            roll_west(ri, ci)

    for ri in range(nrows - 1, -1, -1):
        for ci in range(ncols):
            roll_south(ri, ci)

    for ci in range(ncols - 1, -1, -1):
        for ri in range(nrows):
            roll_east(ri, ci)

def part2():
    loads = []
    for _ in range(500):
        cycle()
        loads.append(calculate_load())

    # hack to try to detect cycle length
    cycle_len = 0
    min_cycle_length = 10
    pat = loads[100:100 + min_cycle_length]
    for i in range(100 + min_cycle_length + 1, 500 - min_cycle_length):
        if loads[i:i+min_cycle_length] == pat:
            cycle_len = i - 100
            break

    remainder = (1_000_000_000 - 100) % cycle_len

    print(f'cycle_len: {cycle_len}')
    print(f'multiplier: {(1_000_000_000 - 100) // cycle_len}')
    print(f'remainder: {remainder}')

    return loads[100 + remainder - 1]

# print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
