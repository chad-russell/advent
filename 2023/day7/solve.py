from functools import cmp_to_key
from itertools import combinations_with_replacement

input = open(0).read().strip().splitlines()
rows = [row.split(' ') for row in input]

cards = '23456789TJQKA'
cards = {c: i for i, c in enumerate(cards)}

def get_rank(hand):
    sh = sorted(hand, key=lambda x: cards[x])
    if sh[0] == sh[4]:
        return 6 # five of a kind
    elif sh[0] == sh[3] or sh[1] == sh[4]:
        return 5 # four of a kind
    elif sh[0] == sh[2] and sh[3] == sh[4] or sh[0] == sh[1] and sh[2] == sh[4]:
        return 4 # full house
    elif sh[0] == sh[2] or sh[1] == sh[3] or sh[2] == sh[4]:
        return 3 # three of a kind
    elif sh[0] == sh[1] and sh[2] == sh[3] or sh[0] == sh[1] and sh[3] == sh[4] or sh[1] == sh[2] and sh[3] == sh[4]:
        return 2 # two pair
    elif sh[0] == sh[1] or sh[1] == sh[2] or sh[2] == sh[3] or sh[3] == sh[4]:
        return 1 # pair
    else:
        return 0 # high card

def part1():
    def compare_rows(r1, r2):
        h1 = r1[0]
        h2 = r2[0]

        rank1 = get_rank(h1)
        rank2 = get_rank(h2)
        if rank1 == rank2:
            for i in range(0, 5):
                i1 = cards[h1[i]]
                i2 = cards[h2[i]]
                if i1 > i2:
                    return 1
                elif i1 < i2:
                    return -1
            return 0
        return -1 if rank2 > rank1 else 1

    sorted_rows = sorted(rows, key=cmp_to_key(compare_rows))

    answer = sum([(ri + 1) * int(r[1]) for ri, r in enumerate(sorted_rows)])

    # assert(answer

    return answer

def part2():
    jcards = 'J23456789TQKA'

    def compare_rows(r1, r2):
        h1 = r1[1]
        h2 = r2[1]

        o1 = r1[0]
        o2 = r2[0]

        rank1 = get_rank(h1)
        rank2 = get_rank(h2)
        if rank1 == rank2:
            for i in range(0, 5):
                i1 = jcards.index(o1[i])
                i2 = jcards.index(o2[i])
                if i1 > i2:
                    return 1
                elif i1 < i2:
                    return -1
            return 0
        return -1 if rank2 > rank1 else 1

    realhands = []
    for hand, bid in rows:
        static_cards = [c[0] for c in hand if c != 'J']
        num_jokers = 5 - len(static_cards)
        if num_jokers == 0:
            realhands.append((hand, hand, bid))
            continue
        best_hand_rank = 0
        best_hand = None
        for combination in combinations_with_replacement('23456789TQKA', num_jokers):
            newhand = ''.join(static_cards) + ''.join(combination)
            newhand_rank = get_rank(newhand)
            if newhand_rank > best_hand_rank:
                best_hand_rank = newhand_rank
                best_hand = newhand
        realhands.append((hand, best_hand, bid))

    sorted_rows = sorted(realhands, key=cmp_to_key(compare_rows))

    answer = sum([(ri + 1) * int(r[2]) for ri, r in enumerate(sorted_rows)])

    # assert(answer == 250506580)

    return answer


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
