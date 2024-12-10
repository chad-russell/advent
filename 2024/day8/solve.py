input = list(map(list, open(0).read().splitlines()))

antennae = dict()
for rowi, row in enumerate(input):
    for coli, col in enumerate(row):
        if col != '.' and col != '#':
            if col in antennae:
                antennae[col].append([rowi, coli])
            else:
                antennae[col] = [[rowi, coli]]

def add_antinode(cur, n) -> bool:
    if (0 <= n[0] < len(input)) and (0 <= n[1] < len(input[0])):
        cur.add(n)
        return True
    return False

def part1():
    antinodes = set()
    for points in antennae.values():
        for i in range(len(points)):
            for j in range(i):
                drow = points[i][0] - points[j][0]
                dcol = points[i][1] - points[j][1]
                add_antinode(antinodes, (points[i][0] + drow, points[i][1] + dcol))
                add_antinode(antinodes, (points[j][0] - drow, points[j][1] - dcol))
    return len(antinodes)

def part2():
    antinodes = set()
    for points in antennae.values():
        for i in range(len(points)):
            for j in range(i):
                drow = points[i][0] - points[j][0]
                dcol = points[i][1] - points[j][1]
                for k in range(len(input)):
                    if not add_antinode(antinodes, (points[i][0] + k * drow, points[i][1] + k * dcol)):
                        break
                for k in range(len(input)):
                    if not add_antinode(antinodes, (points[i][0] - k * drow, points[i][1] - k * dcol)):
                        break
    return len(antinodes)

print(f'part 1: {part1()}') # 303
print(f'part 2: {part2()}') # 1045
