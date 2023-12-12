MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

input = open(0).read().strip().splitlines()

def make_trial(gg):
    a = gg.strip().split(' ')
    return (int(a[0]), a[1])

def make_game(g):
    return [make_trial(gg) for gg in g.split(',')]

def make_game_list(ind, row):
    games = [make_game(g) for g in row.split(':')[1].split(';')]
    return (ind, games)

def is_valid(game):
    for trial in game[1]:
        for result in trial:
            if result[1] == 'red' and result[0] > MAX_RED:
                return False
            elif result[1] == 'green' and result[0] > MAX_GREEN:
                return False
            elif result[1] == 'blue' and result[0] > MAX_BLUE:
                return False
    return True

def power(game):
    min_red = 0
    min_green = 0
    min_blue = 0
    for trial in game[1]:
        for result in trial:
            if result[1] == 'red' and result[0] > min_red:
                min_red = result[0]
            if result[1] == 'green' and result[0] > min_green:
                min_green = result[0]
            if result[1] == 'blue' and result[0] > min_blue:
                min_blue = result[0]
    return min_red * min_green * min_blue

games = [make_game_list(ind + 1, row) for ind, row in enumerate(input)]

def part1():
    answer = sum([game[0] for game in games if is_valid(game)])
    # assert(answer == 2600)
    return answer

def part2():
    answer = sum([power(game) for game in games])
    # assert(answer == 86036)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
