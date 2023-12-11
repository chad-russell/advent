input = open(0).read().strip().splitlines()

d = {'A': 'X', 'B': 'Y', 'C': 'Z'}

move_scores = { 'X': 1, 'Y': 2, 'Z': 3 }
winners = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
losers = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}

game_scores = {
    'XX': 3,
    'YY': 3,
    'ZZ': 3,
    'XY': 6,
    'YZ': 6,
    'ZX': 6,
    'XZ': 0,
    'YX': 0,
    'ZY': 0,
}

def part1():
    answer = 0
    for line in input:
        a, b = line.split(' ')
        s1 = move_scores[b]
        s2 = game_scores[d[a]+ b]
        answer += s1 + s2
    # assert(part1 == 10404)
    return answer

def part2():
    answer = 0
    for line in input:
        a, b = line.split(' ')
        a = d[a]
        if b == 'X':
            answer += move_scores[losers[a]]
        elif b == 'Y':
            answer += 3 + move_scores[a]
        elif b == 'Z':
            answer += 6 + move_scores[winners[a]]
    # assert(part2 == 10334)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
