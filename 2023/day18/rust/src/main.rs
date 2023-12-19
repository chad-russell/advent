use advent::*;
use std::collections::{BTreeMap, BTreeSet};

fn part1_dir_n(line: &str) -> (&str, isize) {
    let mut s = line.split(" ");

    let dir = s.next().unwrap();
    let n = s.next().unwrap().parse::<isize>().unwrap();

    (dir, n)
}

fn part2_dir_n(line: &str) -> (&str, isize) {
    let mut s = line.split(" ");

    let color = s.nth(2).unwrap();
    let color = &color[2..8];

    let dir = &color[5..6];
    let dir = match dir {
        "0" => "R",
        "1" => "D",
        "2" => "L",
        "3" => "U",
        _ => unreachable!(),
    };

    let n = &color[0..5];
    let n = isize::from_str_radix(n, 16).unwrap();

    (dir, n)
}

fn helper(dir_n: &dyn Fn(&str) -> (&str, isize)) -> isize {
    let input = read_input();
    let mut cur = (0, 0);
    let (mut min_x, mut max_x, mut min_y, mut max_y) = (0, 0, 0, 0);
    let mut rowspans = BTreeMap::<isize, Vec<(isize, isize)>>::new();
    let mut up_cache = BTreeSet::<(isize, isize)>::new();

    for line in input.iter() {
        let (dir, n) = dir_n(line);

        match dir {
            "R" => {
                rowspans.entry(cur.0).or_default().push((cur.1, cur.1 + n));
                cur = (cur.0, cur.1 + n);
            }
            "L" => {
                rowspans.entry(cur.0).or_default().push((cur.1 - n, cur.1));
                cur = (cur.0, cur.1 - n)
            }
            "D" => {
                for x in cur.0 + 1..cur.0 + n {
                    rowspans.entry(x).or_default().push((cur.1, cur.1));
                }
                cur = (cur.0 + n, cur.1);
                up_cache.insert((cur.0 - 1, cur.1));
            }
            "U" => {
                up_cache.insert((cur.0 - 1, cur.1));
                for x in cur.0 - n + 1..cur.0 {
                    rowspans.entry(x).or_default().push((cur.1, cur.1));
                }
                cur = (cur.0 - n, cur.1);
            }
            _ => unreachable!(),
        }

        min_x = min_x.min(cur.1);
        max_x = max_x.max(cur.1);
        min_y = min_y.min(cur.0);
        max_y = max_y.max(cur.0);
    }

    let mut n_inside = 0;

    for row in min_y..=max_y {
        let mut inside = false;

        let spans = rowspans.get_mut(&row).unwrap();
        spans.sort_by_key(|a| a.0);

        let mut prev_span_end: Option<isize> = None;

        for (begin, end) in spans.iter() {
            if inside {
                if let Some(prev_span_end) = prev_span_end {
                    n_inside += begin - prev_span_end - 1;
                }
            }

            if begin == end {
                n_inside += 1;
                inside = !inside;
            } else {
                n_inside += end - begin + 1;
                let begin_is_up = up_cache.contains(&(row - 1, *begin));
                let end_is_up = up_cache.contains(&(row - 1, *end));
                if begin_is_up != end_is_up {
                    inside = !inside;
                }
            }

            prev_span_end = Some(*end);
        }
    }

    n_inside
}

fn part1() -> isize {
    let answer = helper(&part1_dir_n);
    // assert!(answer == 47045);
    answer
}

fn part2() -> isize {
    let answer = helper(&part2_dir_n);
    // assert!(answer == 147839570293376);
    answer
}

fn main() {
    println!("part 1: {}", part1());
    println!("part 2: {}", part2());
}
