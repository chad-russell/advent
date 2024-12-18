input = list(map(list, open(0).read().strip().splitlines()))

nrows = len(input)
ncols = len(input[0])

possible_heads = [(rowi, coli) for rowi, row in enumerate(input) for coli, col in enumerate(row) if col == '0']

def extend_boundary(boundary, next, empty, add):
    new_boundary = empty
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in boundary:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols and input[nr][nc] == next:
                add(new_boundary, (nr, nc))
    return new_boundary

def score_rating(ph, constructor, add_fn):
    boundary = constructor([ph])
    next = 1
    while True:
        new_boundary = extend_boundary(boundary, str(next), constructor(), add_fn)
        if new_boundary == boundary or len(new_boundary) == 0:
            break
        boundary = new_boundary
        next += 1
    return len(boundary) if next == 10 else 0

def part1():
    return sum(score_rating(ph, constructor=set, add_fn=lambda cur, n: cur.add(n)) for ph in possible_heads)

def part2():
    return sum(score_rating(ph, constructor=list, add_fn=lambda cur, n: cur.append(n)) for ph in possible_heads)

print(f'part 1: {part1()}') # 646
print(f'part 2: {part2()}') # 1494
