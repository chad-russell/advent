from heapq import heapify, heappush, heappop

input = open(0).read().splitlines()

def index_input(r, c):
    return input[r % len(input)][c % len(input[0])]

def in_bounds(r, c):
    return r >= 0 and r < len(input) and c >= 0 and c < len(input[0])

sr, sc = 0, 0

for ri, r in enumerate(input):
    for ci, c in enumerate(r):
        if c == 'S':
            sr, sc = ri, ci

def helper(n, part):
    cur = set()
    cur.add((sr, sc))

    next = set()

    for _ in range(n):
        for r, c in cur:
            options = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for nr, nc in options:
                if part == 1:
                    if not in_bounds(nr, nc):
                        continue
                    if input[nr][nc] in '.S':
                        next.add((nr, nc))
                else:
                    if index_input(nr, nc) in '.S':
                        next.add((nr, nc))
        cur, next = next, cur
        next.clear()

    return len(cur)


def part1():
    answer = helper(64, part=1)
    # assert(answer == 3503)
    return answer

# Lagrangian interpolation formula for quadratic coefficients
def quad_interp(values):
    return (
        values[0] / 2 - values[1] + values[2] / 2,
        -3 * (values[0] / 2) + 2 * values[1] - values[2] / 2,
        values[0]
    )

def part2_reddit():
    # Magic numbers -- 65 == distance to edge of board, 131 == width of board (including edges for off-by-one nonsense)
    values = [helper(n, part=2) for n in (65, 65 + 131, 65 + 131 * 2)]
    coeffs = quad_interp(values)
    target = (26_501_365 - 65) / 131
    answer = int(coeffs[0] * target * target + coeffs[1] * target + coeffs[2])
    # assert(answer == 584211423220706)
    return answer

print(f'part 1: {part1()}')
print(f'reddit: {part2_reddit()}')
