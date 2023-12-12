use nom::{
    bytes::complete::tag,
    character::complete::{self, alpha1, digit1, line_ending},
    combinator::map_res,
    multi::separated_list1,
    sequence::{preceded, separated_pair},
    IResult,
};

static MAX_RED: u32 = 12;
static MAX_GREEN: u32 = 13;
static MAX_BLUE: u32 = 14;

#[derive(Debug)]
enum Color {
    Red,
    Green,
    Blue,
}

impl From<&str> for Color {
    fn from(s: &str) -> Self {
        match s {
            "red" => Color::Red,
            "green" => Color::Green,
            "blue" => Color::Blue,
            _ => unreachable!(),
        }
    }
}

#[derive(Debug)]
struct Cube {
    amount: u32,
    color: Color,
}

#[derive(Debug)]
struct Round {
    cubes: Vec<Cube>,
}

#[derive(Debug)]
struct Game {
    id: u32,
    rounds: Vec<Round>,
}

impl Game {
    fn is_valid(&self) -> bool {
        for trial in self.rounds.iter() {
            for result in trial.cubes.iter() {
                match result.color {
                    Color::Red if result.amount > MAX_RED => {
                        return false;
                    }
                    Color::Green if result.amount > MAX_GREEN => {
                        return false;
                    }
                    Color::Blue if result.amount > MAX_BLUE => {
                        return false;
                    }
                    _ => {}
                }
            }
        }

        true
    }

    fn power(&self) -> u32 {
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;

        for round in self.rounds.iter() {
            for cube in round.cubes.iter() {
                match cube.color {
                    Color::Red => {
                        if cube.amount > red {
                            red = cube.amount;
                        }
                    }
                    Color::Green => {
                        if cube.amount > green {
                            green = cube.amount;
                        }
                    }
                    Color::Blue => {
                        if cube.amount > blue {
                            blue = cube.amount;
                        }
                    }
                }
            }
        }

        red * green * blue
    }
}

fn color(input: &str) -> IResult<&str, Color> {
    let (input, color) = alpha1(input)?;
    Ok((input, Color::from(color)))
}

fn cube(input: &str) -> IResult<&str, Cube> {
    let (input, (amount, color)) = separated_pair(complete::u32, tag(" "), color)(input)?;
    Ok((input, Cube { amount, color }))
}

fn round(input: &str) -> IResult<&str, Round> {
    let (input, cubes) = separated_list1(tag(", "), cube)(input)?;
    Ok((input, Round { cubes }))
}

fn game(input: &str) -> IResult<&str, Game> {
    let (input, id) = preceded(tag("Game "), map_res(digit1, str::parse))(input)?;
    let (input, _) = tag(": ")(input)?;
    let (input, rounds) = separated_list1(tag("; "), round)(input)?;
    Ok((input, Game { rounds, id }))
}

fn parser(input: &str) -> IResult<&str, Vec<Game>> {
    separated_list1(line_ending, game)(input)
}

fn parse_games() -> Vec<Game> {
    let filename = std::env::args().nth(1).unwrap();
    let input = std::fs::read_to_string(filename).unwrap();
    let (_, games) = parser(input.as_str()).unwrap();
    games
}

fn part1() -> u32 {
    let answer = parse_games()
        .iter()
        .filter(|game| game.is_valid())
        .map(|game| game.id)
        .sum::<u32>();

    // assert!(answer == 2600);

    answer
}

fn part2() -> u32 {
    let answer = parse_games().iter().map(|game| game.power()).sum::<u32>();

    // assert!(answer == 86036)

    answer
}

fn main() {
    println!("part 1: {}", part1());
    println!("part 2: {}", part2());
}
