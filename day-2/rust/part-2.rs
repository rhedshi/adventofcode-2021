#!/usr/bin/env cargo-script

use std::io;

fn main() {
    let mut aim = 0;
    let mut position = 0;
    let mut depth = 0;

    loop {
        let mut input = String::new();
        match io::stdin().read_line(&mut input) {
            Ok(n) => {
                if n == 0 {
                    break;
                }
                input = input.trim().to_string();
            }
            Err(error) => {
                eprintln!("{}", error);
            }
        }

	let mut iter = input.split_whitespace();

        let direction = iter.next().unwrap();
        let distance = iter.next().unwrap().parse::<i32>().unwrap();

        match direction {
            "forward" => {
                position += distance;
                depth += aim * distance;
            },
            "down" => aim += distance,
            "up" => aim -= distance,
            _ => (),
        }
    }

    println!("{}", position * depth);
}

// Answer: 1963088820
