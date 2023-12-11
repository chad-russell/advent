input = open(0).read().strip().splitlines()

def read_map(input, line):
    map = []
    while line < len(input) and len(input[line]) and input[line][0].isdigit():
        m = [int(s) for s in input[line].split(' ')]
        map.append(m)
        line += 1
    return map, line + 2

def read_maps():
    seeds = input[0].split(':')[1].strip().split(' ')
    seeds = [int(s) for s in seeds]
    line = 3
    seed_to_soil, line = read_map(input, line)
    soil_to_fertilizer, line = read_map(input, line)
    fertilizer_to_water, line = read_map(input, line)
    water_to_light, line = read_map(input, line)
    light_to_temperature, line = read_map(input, line)
    temperature_to_humidity, line = read_map(input, line)
    humidity_to_location, line = read_map(input, line)
    r = {
            'seeds': seeds,
            'seed-to-soil': seed_to_soil,
            'soil-to-fertilizer': soil_to_fertilizer,
            'fertilizer-to-water': fertilizer_to_water,
            'water-to-light': water_to_light,
            'light-to-temperature': light_to_temperature,
            'temperature-to-humidity': temperature_to_humidity,
            'humidity-to-location': humidity_to_location
            }
    return r

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

maps = read_maps()

def part1():
    lowest = 2**64
    for seed in maps['seeds']:
        location = lookup_location(seed, maps)
        lowest = min(lowest, location)
    # assert(lowest == 340994526)
    return lowest

def part2():
    seeds = maps['seeds']
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for m in list(maps.values())[1:]:
        new_seed_ranges = []

        while len(seed_ranges) > 0:
            s, e = seed_ranges.pop()
            assert(s < e)

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

