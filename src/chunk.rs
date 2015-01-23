#![allow(dead_code)]
mod chunk {

    use std::fmt;
    use std::rc::Rc;
    use std::rc::Weak;

    struct Address {
        x: u64,
        y: u64,
        z: u64,
    }

    struct Element {
        name: String,
    }

    struct Chunk {
        address: Address,
        children: [Option<Rc<Chunk>>; 8],
        entities: Vec<Rc<Entity>>,
        parent: Option<Weak<Chunk>>,
        scale: u8,
        summary: Rc<Element>,
        mass: f64,
        center: Vec3f64,
    }

    impl Address {
        fn from_string(address: String) -> Option<Address> {
            let mut xyz: (u64, u64, u64) = (1, 1, 1);
            let mut xyz_add: (u64, u64, u64);

            for (i, c) in address.chars().enumerate() {
                if i > 63 {
                    break;
                }
                xyz_add =  match c.to_digit(8) {
                    Some(0) => (0, 0, 0),
                    Some(1) => (0, 0, 1),
                    Some(2) => (0, 1, 0),
                    Some(3) => (0, 1, 1),
                    Some(4) => (1, 0, 0),
                    Some(5) => (1, 0, 1),
                    Some(6) => (1, 1, 0),
                    Some(7) => (1, 1, 1),
                    _ => return None,
                };
                xyz = (xyz.0 << 1, xyz.1 << 1, xyz.2 << 1);
                xyz = (xyz.0 + xyz_add.0, xyz.1 + xyz_add.1, xyz.2 + xyz_add.2);
            }
            Some(Address {x: xyz.0, y: xyz.1, z: xyz.2})
        }
    }

    impl ToString for Address {
        fn to_string(&self) -> String {
            String::from_str("")
        }
    }

    impl PartialEq for Address {
        fn eq(&self, other: &Self) -> bool {
            (((self.x == other.x) && (self.y == other.y)) && (self.z == other.z))
        }
    }

    impl fmt::Show for Address {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "Address({}, {}, {})", self.x, self.y, self.z)
        }
    }

    impl Chunk {
        fn get_child(&self, x: u8, y: u8, z:u8) -> Option<Rc<Chunk>> {
            match (x, y, z) {
                (0, 0, 0) => self.children[0],
                (0, 0, 1) => self.children[1],
                (0, 1, 0) => self.children[2],
                (0, 1, 1) => self.children[3],
                (1, 0, 0) => self.children[4],
                (1, 0, 1) => self.children[5],
                (1, 1, 0) => self.children[6],
                (1, 1, 1) => self.children[7],
                _ => None,
            }
        }

        fn orphan(&self, child: Rc<Chunk>) {
        }

        fn emancipate(&self) {
        }

        fn tick(&self, time_delta: f64) {
        }
    }

    #[test]
    fn test_adder_from_string() {
        let known = Option::Some(Address {x: 0b11, y: 0b11, z: 0b11});
        let unknown = Address::from_string(String::from_str("7"));
        assert_eq!(known, unknown)
    }
}
