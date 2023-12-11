use advent::*;

fn parse_map<'a>(lines: &mut impl Iterator<Item = &'a String>) -> Vec<(i64, i64, i64)> {
    let mut map = Vec::new();

    while let Some(line) = lines.next() {
        if line.is_empty() {
            break;
        } else {
            let mut parts = line.split(" ");
            let dst = parts.next().unwrap().parse().unwrap();
            let src = parts.next().unwrap().parse().unwrap();
            let len = parts.next().unwrap().parse().unwrap();
            map.push((dst, src, len));
        }
    }

    return map;
}

fn parse_input() -> (Vec<i64>, Vec<Vec<(i64, i64, i64)>>) {
    let lines = read_input();
    let mut lines = lines.iter();

    // Parse seeds
    let seeds = lines.next();
    let seeds = seeds
        .unwrap()
        .split(":")
        .nth(1)
        .unwrap()
        .trim()
        .split(" ")
        .map(|s| s.parse::<i64>().unwrap())
        .collect::<Vec<_>>();
    lines.next(); // skip empty line

    // Parse maps
    let mut maps = Vec::new();
    while let Some(_) = lines.next() {
        maps.push(parse_map(&mut lines));
    }

    (seeds, maps)
}

fn part1() -> i64 {
    let (seeds, maps) = parse_input();

    let mut lowest = i64::MAX;

    for &seed in seeds.iter() {
        let mut cur_seed = seed;

        for map in maps.iter() {
            for &(dst, src, len) in map.iter() {
                if cur_seed >= src && cur_seed < src + len {
                    cur_seed += dst - src;
                    break;
                }
            }
        }

        if cur_seed < lowest {
            lowest = cur_seed;
        }
    }

    // assert!(lowest == 340994526);

    lowest
}

fn part2() -> i64 {
    let (seeds, maps) = parse_input();

    let mut ranges_to_map = seeds
        .chunks(2)
        .map(|s| (s[0], s[0] + s[1]))
        .collect::<Vec<_>>();
    let mut mapped_ranges = Vec::new();

    // For each map, map all ranges in ranges_to_map
    for map in maps.iter() {
        while let Some(m @ (ss, se)) = ranges_to_map.pop() {
            // Map the range. This may involve splitting the range into multiple ranges,
            // and handling them separately. I.e. if only one part of the range is mapped,
            // then split the range into two. Add the mapped part to mapped_ranges, and the unmapped to
            // ranges_to_map
            let mut mapped = false;

            for &(dst, src, len) in map.iter() {
                let ms = src;
                let me = src + len;

                // If there's no overlap, continue to the next one
                if se <= ms || ss >= me {
                    continue;
                }

                // Otherwise there is some overlap. So We're gonna map in some way
                mapped = true;

                let offset = dst - src;

                if ss >= ms && se <= me {
                    // If the seed is completely contained in the mapped range, then it's easy
                    mapped_ranges.push((ss + offset, se + offset));
                } else if ss < ms && se > me {
                    // There's overlap on both sides
                    ranges_to_map.push((ss, ms));
                    mapped_ranges.push((ms + offset, me + offset));
                    ranges_to_map.push((me, se));
                } else if ss < ms {
                    // Seed starts before the mapped range, continues inside it
                    ranges_to_map.push((ss, ms));
                    mapped_ranges.push((ms + offset, se + offset));
                } else {
                    // Seed starts inside the mapped range, continues after it
                    mapped_ranges.push((ss + offset, me + offset));
                    ranges_to_map.push((me, se));
                }
            }

            if !mapped {
                mapped_ranges.push(m);
            }
        }

        std::mem::swap(&mut mapped_ranges, &mut ranges_to_map);
    }

    let mut lowest = i64::MAX;
    for (s, _) in ranges_to_map {
        if s < lowest {
            lowest = s;
        }
    }

    // assert!(lowest == 52210644);

    lowest
}

fn main() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}
