input = open(0).read().splitlines()

def maybe_operational(n):
    return n in '.?'

def maybe_damaged(n):
    return n in '#?'

memo = {}
def count_ways(given, targets):
    if (given, str(targets)) in memo:
        return memo[(given, str(targets))]

    if len(targets) == 0:
        return all(maybe_operational(g) for g in given)

    target = targets[0]
    if len(given) < target:
        return 0

    count = 0

    last_possible_start = len(given) - target
    if '#' in given:
        last_possible_start = min(last_possible_start, given.index('#'))

    for start in range(last_possible_start + 1):
        all_maybe_damaged = all(maybe_damaged(g) for g in given[start:start + target])
        next_maybe_operational = start + target == len(given) or maybe_operational(given[start + target])
        if all_maybe_damaged and next_maybe_operational:
            count += count_ways(given[start + target + 1:], targets[1:])

    memo[(given, str(targets))] = count
    return count

def part1():
    answer = 0
    for line in input:
        given, target = line.split(' ')
        targets = list(map(int, target.split(',')))
        answer += count_ways(given, targets)

    # assert(answer == 7047)

    return answer

def part2():
    answer = 0
    for line in input:
        given, target = line.split(' ')
        given = '?'.join([given] * 5)
        target = ','.join([target] * 5)
        targets = list(map(int, target.split(',')))
        answer += count_ways(given, targets)

    # assert(answer == 17391848518844)

    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
