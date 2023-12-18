from heapq import heappush, heappop

input = open(0).read().splitlines()
input = [list(map(int, row)) for row in input]

END_COORDS = (len(input) - 1, len(input[0]) - 1)

def out_of_bounds(p):
    return p[0] < 0 or p[1] < 0 or p[0] >= len(input) or p[1] >= len(input[0])

def neighbors(row, col, drow, dcol, streak, max_streak, min_streak):
    n = []
    for ndrow, ndcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nrow, ncol = row + ndrow, col + ndcol

        if out_of_bounds((nrow, ncol)):
            continue

        if (ndrow, ndcol) == (-drow, -dcol):
            continue

        nstreak = 1
        if (ndrow, ndcol) == (drow, dcol) or (drow, dcol) == (0, 0):
            if streak >= max_streak:
                continue
            nstreak = streak + 1
        elif streak < min_streak:
            continue

        n.append((nrow, ncol, ndrow, ndcol, nstreak))

    return n

def debug_printout(path_end, reached):
    path_printout = [['.'] * len(r) for r in input]

    cur = path_end
    while cur:
        path_printout[cur[0]][cur[1]] = input[cur[0]][cur[1]]
        cur = reached[cur]

    for row in path_printout:
        print(''.join(map(str, row)))

def helper(max_streak, min_streak=0):
    start = (0, 0, 0, 0, 0) # row, col, drow, dcol, streak

    frontier = [(0, start)]

    reached = {}
    reached[start] = None

    while frontier:
        (cur_cost, cur_pos) = heappop(frontier)
        row, col, drow, dcol, streak = cur_pos
        if (row, col) == END_COORDS and streak > min_streak:
            # debug_printout(cur_pos, reached)
            # assert(cur_cost == 758)
            return cur_cost
        for next in neighbors(row, col, drow, dcol, streak, max_streak, min_streak):
            if next in reached:
                continue
            next_cost = cur_cost + input[next[0]][next[1]]
            heappush(frontier, (next_cost, next))
            reached[next] = cur_pos

def part1():
    answer = helper(max_streak=3)
    # assert(answer == 758)
    return answer

def part2():
    answer = helper(max_streak=10, min_streak=4)
    # assert(answer == 892)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
