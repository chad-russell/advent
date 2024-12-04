input = open(0).read().splitlines()

width = len(input[0])
height = len(input)

def search1(x, y, dx, dy):
    in_bounds = 0 <= x + dx * 3 < width and 0 <= y + 3 * dy < height
    return in_bounds and all(input[y + dy * i][x + dx * i] == 'XMAS'[i] for i in range(1, 4))

def part1():
    directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if [dx, dy] != [0, 0]]
    return sum(search1(x, y, dx, dy) for x in range(0, width) for y in range(0, height) if input[y][x] == 'X' for dx, dy in directions)

def search2(x, y):
    corners = "".join([input[y - 1][x - 1], input[y - 1][x + 1], input[y + 1][x + 1], input[y + 1][x - 1]])
    return corners in ["MMSS", "MSSM", "SSMM", "SMMS"]

def part2():
    return sum(search2(x, y) for x in range(1, width - 1) for y in range(1, height - 1) if input[y][x] == 'A')

print(f'part 1: {part1()}') # 2662
print(f'part 2: {part2()}') # 2034
