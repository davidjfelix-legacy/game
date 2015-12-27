extern crate mio;

mod chunk;
mod entity;

fn main() {
    let mut event_loop = mio::EventLoop::new().unwrap();
    event_loop.run()
}
