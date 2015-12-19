extern crate mio;

mod chunk;
mod entity;

fn main() {
    let mut x = 0;
    loop {
        print!("{}\r", x);
        x += 1;
    }
}
