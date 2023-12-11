input = open(0).read().strip().splitlines()

def read_nums(nums):
    return [int(n) for n in nums.strip().split(' ') if n != '']

def card_num(row):
    card = row.split(':')[1].strip().split('|')
    winning, have = read_nums(card[0]), read_nums(card[1])
    return len([h for h in have if h in winning])

def card_score(row):
    cn = card_num(row)
    return 2 ** (cn - 1) if cn > 0 else 0

def part1():
    answer = sum([card_score(row) for row in input])
    # assert(answer == 24175)
    return answer

def part2():
    scores = [card_num(row) for row in input]
    cards = [1] * len(input)
    for ci, c in enumerate(cards):
        for i in range(ci + 1, ci + 1 + scores[ci]):
            cards[i] += c
    answer = sum(cards)
    # assert(answer == 18846301)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')

