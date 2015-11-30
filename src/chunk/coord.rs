pub struct Coord {
    x: u8,
    y: u8,
    z: u8
}

pub enum CoordErr {
    OutOfBounds
}

pub type CoordResult = Result<Coord, CoordErr>;

impl Coord {
    fn new(x: u8, y: u8, z: u8) -> CoordResult {
        match (x, y, z) {
            (0, 0, 0) |
            (0, 0, 1) |
            (0, 1, 0) |
            (0, 1, 1) |
            (1, 0, 0) |
            (1, 0, 1) |
            (1, 1, 0) |
            (1, 1, 1) => Ok(Coord{ x: x, y: y, z: z}),
            _ => Err(CoordErr::OutOfBounds)
        }
    }
}
