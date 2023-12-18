from heapq import heappush, heappop

input = open(0).read().splitlines()
input = [list(map(int, row)) for row in input]

def out_of_bounds(p):
    return p[0] < 0 or p[1] < 0 or p[0] >= len(input) or p[1] >= len(input[0])

def neighbors(row, col, drow, dcol, streak):
    n = []
    for ndrow, ndcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nstreak = 1
        if (ndrow, ndcol) == (drow, dcol):
            if streak > 2:
                continue
            nstreak = streak + 1
        if out_of_bounds((row + ndrow, col + ndcol)):
            continue
        if (ndrow, ndcol) == (-drow, -dcol):
            continue

        n.append((row + ndrow, col + ndcol, ndrow, ndcol, nstreak))

    return n

# row, col, drow, dcol, streak
START = (0, 0, 0, 0, 0)

END = (len(input) - 1, len(input[0]) - 1)

frontier = []
heappush(frontier, (0, START))

reached = {}
reached[START] = None

while frontier:
    (cur_cost, cur_pos) = heappop(frontier)
    row, col, drow, dcol, streak = cur_pos
    if (col, row) == END:
        print(f'Total cost: {cur_cost}\n')
        break
    for next in neighbors(row, col, drow, dcol, streak):
        (nrow, ncol, ndrow, ndcol, nstreak) = next
        if next in reached:
            continue
        next_cost = cur_cost + input[next[0]][next[1]]
        heappush(frontier, (next_cost, next))
        reached[next] = cur_pos

path_printout = [['.'] * len(r) for r in input]
