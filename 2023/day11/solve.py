input = open(0).read().strip().splitlines()

empty_rows = [r for r, row in enumerate(input) if all(ch == '.' for ch in row)]
empty_cols = [c for c in range(len(input[0])) if all(row[c] == '.' for row in input)]
galaxy_coords = [(r, c) for r, row in enumerate(input) for c, col in enumerate(row) if col == '#']

def expanded(p, n):
    return (
        p[0] + (n - 1) * sum(r < p[0] for r in empty_rows), 
        p[1] + (n - 1) * sum(c < p[1] for c in empty_cols)
    )

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(n):
    exp_coords = [expanded(c, n) for c in galaxy_coords]
    combs = [(a, b) for ai, a in enumerate(exp_coords) for b in exp_coords[:ai]]
    return sum([manhattan(a, b) for a, b in combs])

def part1():
    answer = solve(2)
    # assert(answer == 9370588)
    return answer

def part2():
    answer = solve(1000000) 
    # assert(answer == 746207878188)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
