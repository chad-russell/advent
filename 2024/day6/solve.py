input = open(0).read().splitlines()

width = len(input[0])
height = len(input)

start_guard_row, start_guard_col = next([rowi, coli] for rowi, row in enumerate(input) for coli, col in enumerate(row) if col == '^')

def is_loop_common(guard_row, guard_col, rowi, coli, check=False):
    dx, dy = 0, -1
    visited = {(guard_row, guard_col, dx, dy) if check else (guard_row, guard_col)}
    while True:
        new_row, new_col = guard_row + dy, guard_col + dx
        if not (0 <= new_col < width and 0 <= new_row < height):
            return [False, visited]
        if (input[new_row][new_col] == '#') or (check and new_row == rowi and new_col == coli):
            dx, dy = -dy, dx
        else:
            guard_row, guard_col = new_row, new_col
            if check and (guard_row, guard_col, dx, dy) in visited:
                return [True, visited]
            visited.add((guard_row, guard_col, dx, dy) if check else (guard_row, guard_col))

def part1():
    _, visited = is_loop_common(start_guard_row, start_guard_col, 0, 0, check=False)
    return len(visited)

def part2():
    _, visited = is_loop_common(start_guard_row, start_guard_col, 0, 0, check=False)
    return sum(1 for (rowi, coli) in visited
        if is_loop_common(start_guard_row, start_guard_col, rowi, coli, check=True)[0])


print(f'part 1: {part1()}') # 5162
print(f'part 2: {part2()}') # 1909
