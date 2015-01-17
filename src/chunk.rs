mod chunk {

    struct Address(u64, u64, u64);

    struct Chunk {
        children: [Option<Box<Chunk>>; 8],
        parent: Option<Box<Chunk>>,
        summary: i32,
        address: Address,
    }

    impl Address {
        fn from_string(&self) -> Address {
            Address(0, 0, 0)
        }

        fn ffs(value: u64) -> u8 {
            let mut mask = value;
            let mut bit: u8 = 0;

            while (mask & 1) != 0 {
                mask = mask >> 1;
                bit += 1;
            }
            bit
        }
    }

    impl ToString for Address {
        fn to_string(&self) -> String {
            String::from_str("")
        }
        
    }
}
