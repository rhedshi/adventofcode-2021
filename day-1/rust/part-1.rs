#!/usr/bin/env cargo-script

use std::io;

fn main() {
    let mut increase = 0;
    let mut current = None::<i32>;

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

        let depth = input.parse::<i32>().unwrap();

        if current.is_some() && depth > current.unwrap() {
            increase += 1;
        }

        current = Some(depth);
    }

    println!("{}", increase);
}

// Answer: 1553
