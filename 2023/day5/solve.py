input = open(0).read().strip().split('\n\n')

def read_entry(line):
    return [int(s) for s in line.split(' ')]

def read_map(input):
    input = input.splitlines()
    name = input[0].split(' ')[0]
    map = [read_entry(line) for line in input[1:]]
    return name, map

def read_input():
    seeds = input[0].split(':')[1].strip().split(' ')
    seeds = [int(s) for s in seeds]
    maps = dict(read_map(m) for m in input[1:])
    return seeds, maps

def lookup(n, map):
    for m in map:
        start = m[1]
        end = m[1] + m[2]
        if n >= start and n < end:
            return m[0] + n - start
    return n

def lookup_location(seed, maps):
    soil = lookup(seed, maps['seed-to-soil'])
    fertilizer = lookup(soil, maps['soil-to-fertilizer'])
    water = lookup(fertilizer, maps['fertilizer-to-water'])
    light = lookup(water, maps['water-to-light'])
    temperature = lookup(light, maps['light-to-temperature'])
    humidity = lookup(temperature, maps['temperature-to-humidity'])
    location = lookup(humidity, maps['humidity-to-location'])
    return location

def chunk(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

seeds, maps = read_input()

def part1():
    lowest = 2**64
    for seed in seeds:
        location = lookup_location(seed, maps)
        lowest = min(lowest, location)
    # assert(lowest == 340994526)
    return lowest

def part2():
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for m in list(maps.values())[1:]:
        new_seed_ranges = []

        while len(seed_ranges) > 0:
            s, e = seed_ranges.pop()

            found = False
            for a, b, c in m:
                shift = a - b

                rs = b
                re = b + c

                os = max(s, rs)
                oe = min(e, re)

                if e <= rs or s >= re:
                    continue
                else:
                    found = True
                    new_seed_ranges.append((os + shift, oe + shift))
                    if s < rs:
                        seed_ranges.append((s, rs))
                    if e > re:
                        seed_ranges.append((re, e))
                    break
            if not found:
                    new_seed_ranges.append((s, e))

        new_seed_ranges = list(set(new_seed_ranges))
        new_seed_ranges.sort()
        
        seed_ranges = new_seed_ranges

    answer = min(seed_ranges)[0]
    # assert(answer == 52210644)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')

