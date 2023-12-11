import math

input = open(0).read().strip().splitlines()

times = input[0].split(':')[1]
times = [int(t) for t in times.split(' ') if t]

distances = input[1].split(':')[1]
distances = [int(d) for d in distances.split(' ') if d]

def part1():
    winning_times = 1
    for td in range(len(times)):
        t = times[td]
        d = distances[td]

        x1 = (-t + math.sqrt(t*t - 4 * d)) / -2
        x2 = (-t - math.sqrt(t*t - 4 * d)) / -2

        x1c = math.ceil(x1)
        x2f = math.floor(x2)

        if x1c == x1:
            x1c += 1
        if x2f == x2:
            x2f -= 1

        winning_times *= x2f - x1c + 1
    # assert(winning_times == 5133600)
    return winning_times


def part2():
    t = int(''.join([str(t) for t in times]))
    d = int(''.join([str(d) for d in distances]))

    x1 = (-t + math.sqrt(t*t - 4 * d)) / -2
    x2 = (-t - math.sqrt(t*t - 4 * d)) / -2

    x1c = math.ceil(x1)
    x2f = math.floor(x2)

    if x1c == x1:
        x1c += 1
    if x2f == x2:
        x2f -= 1

    answer = x2f - x1c + 1
    # assert(answer == 40651271)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
