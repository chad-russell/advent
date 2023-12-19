use std::env;

pub fn read_input() -> Vec<String> {
    let filename = env::args().nth(1).unwrap();
    let input = std::fs::read_to_string(filename).unwrap();
    input
        .trim()
        .split("\n")
        .map(|l| l.trim().to_string())
        .collect::<Vec<_>>()
}
