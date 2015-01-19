#![allow(dead_code)]
mod chunk {

    struct Address(u64, u64, u64);

    struct Chunk {
        children: [Option<Box<Chunk>>; 8],
        parent: Option<Box<Chunk>>,
        summary: i32,
        address: Address,
    }

    impl Address {
        fn from_string(address: String) -> Address {
            let mut x: u64 = 1;
            let mut y: u64 = 1;
            let mut z: u64 = 1;
            let mut xadd: u8 = 0;
            let mut yadd: u8 = 0;
            let mut zadd: u8 = 0;

            for (i, c) in address.split_str("").enumerate() {
                if i > 63 {
                    break;
                }
                let (xadd, yadd, zadd) = match c {
                    "0" => (0, 0, 0),
                    "1" => (0, 0, 1),
                    "2" => (0, 1, 0),
                    "3" => (0, 1, 1),
                    "4" => (1, 0, 0),
                    "5" => (1, 0, 1),
                    "6" => (1, 1, 0),
                    "7" => (1, 1, 1),
                    _ => (0,0,0),
                };
                (x, y, z) = (x << 1, y << 1, z << 1)
                (x, y, z) = (x + xadd, y + yadd, z + zadd)
            }
            Address(x, y, z)
        }
    }

    impl ToString for Address {
        fn to_string(&self) -> String {
            String::from_str("")
        }
        
    }
}
