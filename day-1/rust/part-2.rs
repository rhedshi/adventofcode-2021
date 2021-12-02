#!/usr/bin/env cargo-script

use std::io;

fn main() {
    let mut increase = 0;

    const N: usize = 3;
    let mut window = [None::<i32>; N];
    let mut i = 0;

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

        if window[i].is_some() && depth > window[i].unwrap() {
            increase += 1;
        }

        window[i] = Some(depth);
        i += 1;
        i %= N;
    }

    println!("{}", increase);
}

// Answer: 1597
