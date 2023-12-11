use advent::*;

fn part1() -> u32 {
    let mut sum = 0;
    for line in read_input() {
        let mut c1 = 0;
        let mut c2 = 0;
        let mut found_digit = false;

        for ch in line.chars() {
            if ch.is_ascii_digit() {
                let dig = ch.to_digit(10).unwrap();
                if !found_digit {
                    c1 = dig;
                    found_digit = true;
                }
                c2 = dig;
            }
        }

        sum += 10 * c1 + c2;
    }

    // assert!(sum == 54667);

    sum
}

fn part2() -> u32 {
    let mut sum = 0;
    for line in read_input() {
        let mut line = line.as_str();

        let mut c1 = 0;
        let mut c2 = 0;
        let mut found_digit = false;

        while !line.is_empty() {
            let ch = line.chars().next().unwrap();
            let mut digit = 0;
            let mut found = false;

            if ch.is_ascii_digit() {
                digit = ch.to_digit(10).unwrap();
                found = true;
            } else {
                if line.starts_with("one") {
                    digit = 1;
                    found = true;
                } else if line.starts_with("two") {
                    digit = 2;
                    found = true;
                } else if line.starts_with("three") {
                    digit = 3;
                    found = true;
                } else if line.starts_with("four") {
                    digit = 4;
                    found = true;
                } else if line.starts_with("five") {
                    digit = 5;
                    found = true;
                } else if line.starts_with("six") {
                    digit = 6;
                    found = true;
                } else if line.starts_with("seven") {
                    digit = 7;
                    found = true;
                } else if line.starts_with("eight") {
                    digit = 8;
                    found = true;
                } else if line.starts_with("nine") {
                    digit = 9;
                    found = true;
                }
            }

            if found {
                if !found_digit {
                    c1 = digit;
                    found_digit = true;
                }
                c2 = digit;
            }

            line = &line[1..];
        }

        sum += 10 * c1 + c2;
    }

    // assert!(sum == 54203);

    sum
}

fn main() {
    println!("part 1: {}", part1());
    println!("part 2: {}", part2());
}
