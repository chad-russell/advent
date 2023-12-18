input = open(0).read().splitlines()

def part1_dir_n(split_line):
    dir, n, _ = split_line
    return dir, int(n)

def part2_dir_n(split_line):
    color = split_line[2]
    color = color[2:-1] # remove the parens and the '#'

    dir = int(color[-1])
    dir = 'RDLU'[dir]

    n = int(color[:-1], 16)

    return dir, n

def present(rowspans, r, c):
    return r in rowspans and any(start <= c <= end for start, end in rowspans[r])

def helper(get_dir_n):
    cur = (0, 0)

    rowspans = {}

    for line in input:
        dir, n = get_dir_n(line.split(' '))

        if dir == 'R':
            if cur[0] not in rowspans:
                rowspans[cur[0]] = []
            rowspans[cur[0]].append((cur[1], cur[1] + n))
            cur = (cur[0], cur[1] + n)
        elif dir == 'L':
            if cur[0] not in rowspans:
                rowspans[cur[0]] = []
            rowspans[cur[0]].append((cur[1] - n, cur[1]))
            cur = (cur[0], cur[1] - n)
        elif dir == 'D':
            for x in range(cur[0] + 1, cur[0] + n):
                if x not in rowspans:
                    rowspans[x] = [(cur[1], cur[1])]
                else:
                    rowspans[x].append((cur[1], cur[1]))
            cur = (cur[0] + n, cur[1])
        elif dir == 'U':
            for x in range(cur[0] - n + 1, cur[0]):
                if x not in rowspans:
                    rowspans[x] = [(cur[1], cur[1])]
                else:
                    rowspans[x].append((cur[1], cur[1]))
            cur = (cur[0] - n, cur[1])

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    for r in rowspans:
        min_y = min(min_y, r)
        max_y = max(max_y, r)
        for start, end in rowspans[r]:
            min_x = min(min_x, start)
            max_x = max(max_x, end)
    

    print(min_y, min_x, max_y, max_x)
    print(len(rowspans))

    n_inside = 0

    # for row in range(0, max_y + 1):
    #     inside = False
    #     spans = rowspans[row]
    #     spans.sort()
    #     print(spans)

    for row in range(0, max_y + 1):
        inside = False
        col = 0
        # srow = []
        while col <= max_x:
            if present(rowspans, row, col):
                start_col = col
                start_is_up = present(rowspans, row - 1, col)

                while present(rowspans, row, col):
                    # srow.append('#')
                    n_inside += 1
                    col += 1

                end_col = col
                end_is_up = present(rowspans, row - 1, col - 1)

                if start_col + 1 == end_col:
                    inside = not inside
                elif start_is_up != end_is_up:
                    inside = not inside
            else:
                col += 1
                # srow.append('#' if inside else '.')
                if inside:
                    n_inside += 1
        # print(''.join(srow))

    return n_inside

def part1():
    answer = helper(part1_dir_n)
    return answer

def part2():
    answer = helper(part2_dir_n)
    return answer

print(f'part 1: {part1()}')
# print(f'part 2: {part2()}')
