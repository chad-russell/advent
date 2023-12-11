from typing import List

input = open(0).read().strip().splitlines()

start = (0, 0)

def out_of_bounds(r, c):
    return r < 0 or c < 0 or r >= len(input) or c >= len(input[0])

for rown, row in enumerate(input):
    for coln, col in enumerate(row):
        if col == 'S':
            start = (rown, coln)

def push_conn(conns, r, c):
    if not out_of_bounds(r, c):
        conns.append((r, c))

def connections(p):
    r, c = p

    conns = []

    if input[r][c] == 'S':
        # check to north
        if input[r - 1][c] in ['|', 'F', '7']:
            conns.append((r - 1, c))
        # check to south
        if input[r + 1][c] in ['|', 'L', 'J']:
            conns.append((r + 1, c))
        # check to west
        if input[r][c - 1] in ['-', 'L', 'F']:
            conns.append((r, c - 1))
        # check to east
        if input[r][c + 1] in ['-', '7', 'J']:
            conns.append((r, c + 1))
    elif input[r][c] == '|':
        push_conn(conns, r - 1, c)
        push_conn(conns, r + 1, c)
    elif input[r][c] == '-':
        push_conn(conns, r, c - 1)
        push_conn(conns, r, c + 1)
    elif input[r][c] == 'L':
        push_conn(conns, r - 1, c)
        push_conn(conns, r, c + 1)
    elif input[r][c] == 'J':
        push_conn(conns, r, c - 1)
        push_conn(conns, r - 1, c)
    elif input[r][c] == '7':
        push_conn(conns, r, c - 1)
        push_conn(conns, r + 1, c)
    elif input[r][c] == 'F':
        push_conn(conns, r, c + 1)
        push_conn(conns, r + 1, c)

    return conns

def part1():
    dist = 0
    distances: List[List[int]] = [[-1] * len(input[0]) for _ in input]
    distances[start[0]][start[1]] = 0

    start_points = [start]
    while start_points:
        dist += 1
        dst_points = []
        for s in start_points:
            dst_points += [(r, c) for (r, c) in connections(s) if distances[r][c] == -1]
        dst_points = set(dst_points)
        for r, c in dst_points:
            distances[r][c] = dist
        start_points = dst_points

    answer = dist - 1

    assert(answer == 6890)

    return answer

def infer_start(s):
    r, c = s

    north = False
    south = False
    east = False
    west = False

    if input[r - 1][c] in ['|', 'F', '7']:
        north = True
    if input[r + 1][c] in ['|', 'L', 'J']:
        south = True
    if input[r][c - 1] in ['-', 'L', 'F']:
        west = True
    if input[r][c + 1] in ['-', '7', 'J']:
        east = True

    if north and south:
        return '|'
    elif east and west:
        return '-'
    elif north and east:
        return 'L'
    elif north and west:
        return 'J'
    elif south and west:
        return '7'
    else:
        assert(south and east)
        return 'F'

def part2():
    dist = 0
    distances: List[List[int]] = [[-1] * len(input[0]) for _ in input]
    distances[start[0]][start[1]] = 0

    inferred_start = infer_start(start)

    start_points = [start]
    while start_points:
        dist += 1
        dst_points = []
        for s in start_points:
            dst_points += [(r, c) for (r, c) in connections(s) if distances[r][c] == -1]
        dst_points = set(dst_points)
        for r, c in dst_points:
            distances[r][c] = dist
        start_points = dst_points

    nrows = []
    for irow, drow in zip(input, distances):
        nrow = ['.' if dr == -1 else ir for (ir, dr) in zip(list(irow), drow)]
        nrows.append(nrow)

    nrows[start[0]][start[1]] = inferred_start

    num_is = 0

    for nr in nrows:
        inside = 0
        i = 0
        while i < len(nr):
            if nr[i] == '.':
                nr[i] = 'I' if inside else 'O'
                i += 1
            elif nr[i] == '|':
                inside = not inside
                i += 1
            elif nr[i] in ['F', '7', 'J', 'L']:
                fst = nr[i]
                i += 1
                while i < len(nr) and nr[i] == '-':
                    i += 1
                assert(nr[i] in ['F', '7', 'J', 'L'])
                snd = nr[i]
                if [fst, snd] == ['L', 'J']:
                    pass # inside-ness unchanged
                elif [fst, snd] == ['L', '7']:
                    inside = not inside
                elif [fst, snd] == ['F', '7']:
                    pass # inside-ness unchanged
                elif [fst, snd] == ['F', 'J']:
                    inside = not inside
                else:
                    print(f'ERROR: [fst, snd] = {[fst, snd]}')
                    assert(False)
                i += 1
            else:
                print(f'ERROR: {i} -> {nr[i]}')
                assert(False)

        i = len(nr) - 1
        while nr[i] == 'I':
            nr[i] = 'O'
            i -= 1

        num_is += len([a for a in nr if a == 'I'])

    assert(num_is == 453)

    return num_is


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
