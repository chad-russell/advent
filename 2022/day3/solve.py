input = open(0).read().strip().splitlines()

def part1():
    sum = 0
    for line in input:
        half = len(line) // 2
        first, second = line[:half], line[half:]
        first = set(first)
        second = set(second)
        common = first & second
        common = common.pop()
        if common.isupper():
            sum += ord(common) - 65 + 27
        else:
            sum += ord(common) - 97 + 1
    return sum

def part2():
    sum = 0
    for i in range(0, len(input), 3):
        common = set(input[i]) & set(input[i + 1]) & set(input[i + 2])
        common = common.pop()
        if common.isupper():
            sum += ord(common) - 65 + 27
        else:
            sum += ord(common) - 97 + 1
    return sum


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
