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

def helper(get_dir_n):
    cur = (0, 0)

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    rowspans = {}

    up_cache = set()

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
            up_cache.add((cur[0] - 1, cur[1]))
        elif dir == 'U':
            up_cache.add((cur[0] - 1, cur[1]))
            for x in range(cur[0] - n + 1, cur[0]):
                if x not in rowspans:
                    rowspans[x] = [(cur[1], cur[1])]
                else:
                    rowspans[x].append((cur[1], cur[1]))
            cur = (cur[0] - n, cur[1])

        min_x = min(min_x, cur[1])
        max_x = max(max_x, cur[1])
        min_y = min(min_y, cur[0])
        max_y = max(max_y, cur[0])
    
    n_inside = 0
    
    for row in range(min_y, max_y + 1):
        inside = False

        spans = rowspans[row]
        spans.sort()

        prev_span_end = None

        for begin, end in spans:
            if inside and prev_span_end != None:
                n_inside += begin - prev_span_end - 1

            if begin == end:
                n_inside += 1
                inside = not inside
            else:
                n_inside += end - begin + 1
                begin_is_up = (row - 1, begin) in up_cache
                end_is_up = (row - 1, end) in up_cache
                if begin_is_up != end_is_up:
                    inside = not inside

            prev_span_end = end

    return n_inside

def part1():
    answer = helper(part1_dir_n)
    # assert(answer == 47045)
    return answer

def part2():
    answer = helper(part2_dir_n)
    # assert(answer == 147839570293376)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
