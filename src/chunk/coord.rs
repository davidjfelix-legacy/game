pub struct Coord {
    x: u8,
    y: u8,
    z: u8
}

pub enum CoordErr {
    OutOfBounds
}

pub type CoordResult = Result<Coord, CoordErr>;
pub type IndexResult = Result<usize, CoordErr>;
pub type CoordVecResult = Result<Vec<Coord>, CoordErr>;

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

    fn to_index(self) -> IndexResult {
        match (self.x, self.y, self.z) {
            (0, 0, 0) => Ok(0),
            (0, 0, 1) => Ok(1),
            (0, 1, 0) => Ok(2),
            (0, 1, 1) => Ok(3),
            (1, 0, 0) => Ok(4),
            (1, 0, 1) => Ok(5),
            (1, 1, 0) => Ok(6),
            (1, 1, 1) => Ok(7),
            _ => Err(CoordErr::OutOfBounds)
        }
    }

    fn copy(self) -> Coord {
        Coord{
            x: self.x,
            y: self.y,
            z: self.z,
        }
    }
}
